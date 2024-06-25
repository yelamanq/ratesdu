from django.http import JsonResponse
from django.shortcuts import render, redirect
from main.models import Schedule
from collections import defaultdict
from main.models import Message, ReadMessage, Course
from main.forms import MessageForm
from datetime import datetime, timedelta
from cabinet.models import Cabinet


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.is_staff:
        schedule = Course.objects.filter(teacher=request.user).values('id', 'code', 'teacher__first_name',
                                                                      'teacher__last_name', 'cabinet__name',
                                                                      'time__start', 'time__end', 'week_day')
    else:
        schedule = Schedule.objects.filter(user=request.user).values('lesson__id', 'lesson__code',
                                                                     'lesson__teacher__first_name',
                                                                     'lesson__teacher__last_name',
                                                                     'lesson__cabinet__name', 'lesson__time__start',
                                                                     'lesson__time__end', 'lesson__week_day')

    # Create a defaultdict to organize lessons by time slots and days of the week
    schedule_table = defaultdict(dict)

    # Map week day index to its abbreviation
    day_mapping = {1: 'Mo', 2: 'Tu', 3: 'We', 4: 'Th', 5: 'Fr', 6: 'Sa', 7: 'Su'}

    # Populate schedule_table with lessons
    for entry in schedule:
        lesson_time = entry['lesson__time__start'] if not request.user.is_staff else entry['time__start']
        week_day = entry['lesson__week_day'] if not request.user.is_staff else entry['week_day']
        day_abbr = day_mapping[week_day]

        if lesson_time not in schedule_table:
            schedule_table[lesson_time] = defaultdict(list)

        schedule_table[lesson_time][day_abbr].append(entry)

    # Generate HTML for the schedule table
    table_html = "<table><tbody><tr><td>Day/Hour</td>"
    for day_abbr in day_mapping.values():
        table_html += f"<td><span>{day_abbr}</span></td>"
    table_html += "</tr>"

    # Define the timeslots
    timeslots = [['09:00', '09:50'], ['10:00', '10:50'], ['11:00', '11:50'], ['12:00', '12:50'], ['13:00', '13:50'],
                 ['14:00', '14:50'], ['15:00', '15:50'], ['16:00', '16:50'], ['17:00', '17:50']]

    for start_time, end_time in timeslots:
        table_html += "<tr>"
        table_html += f"<td><span>{start_time}</span><br><span>{end_time}</span></td>"
        for day_abbr in day_mapping.values():
            day_lessons = schedule_table.get(start_time, {}).get(day_abbr, [])
            if day_lessons:
                lesson = day_lessons[0]  # Assuming only one lesson per time slot
                table_html += f"<td onclick='openLink({lesson['lesson__id'] if not request.user.is_staff else lesson['id']})'><a>{lesson['lesson__code'] if not request.user.is_staff else lesson['code']}</a><span>{'<br>' + lesson['lesson__teacher__first_name'] if not request.user.is_staff else ''} {lesson['lesson__teacher__last_name'][0] + '.' if not request.user.is_staff else ''}</span><br><span>{lesson['lesson__cabinet__name'] if not request.user.is_staff else lesson['cabinet__name']}</span></td>"
            else:
                table_html += "<td></td>"
        table_html += "</tr>"

    table_html += "</tbody></table>"

    user_lessons = Schedule.objects.filter(user=request.user).values_list('lesson', flat=True)
    unread_messages = Message.objects.exclude(readmessage__user=request.user).filter(lesson__in=user_lessons).values(
        'id', 'title', 'content', 'teacher__first_name', 'teacher__last_name')
    data = {
        "schedule": [
            {
                'code': i['lesson__code'] if not request.user.is_staff else i['code'],
                'teacher': i['lesson__teacher__first_name'] if not request.user.is_staff else i['teacher__first_name'],
                'cabinet': i['lesson__cabinet__name'] if not request.user.is_staff else i['cabinet__name'],
                'time': f"{i['lesson__time__start']}:{i['lesson__time__end']}" if not request.user.is_staff else f"{i['time__start']}:{i['time__end']}",
            } for i in schedule
        ],
        "schedule_table": table_html,
        "messages": [
            {
                'id': i['id'],
                'title': i['title'],
                'content': i['content'],
                'teacher': f"{i['teacher__first_name']} {i['teacher__last_name']}",
            } for i in unread_messages
        ]
    }

    return render(request, 'main/index.html', data)


def read(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = Message.objects.get(id=message_id)
        read_message = ReadMessage(user=request.user, message=message)
        read_message.save()

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


def lesson(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('main')

    if pk is None:
        return redirect('main')

    lesson = Course.objects.get(id=pk)
    students = Schedule.objects.filter(lesson=lesson).values('user__first_name', 'user__last_name', 'user__email')

    form = MessageForm()

    data = {
        'form': form,
        'name': lesson.name,
        'code': lesson.code,
        'teacher': f"{lesson.teacher.first_name} {lesson.teacher.last_name}",
        'cabinet': lesson.cabinet.name,
        'time': f"{lesson.time.start}:{lesson.time.end}",
        'week_day': lesson.week_day,
        'students': students
    }

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            lesson = Course.objects.get(id=pk)
            form.save(teacher=request.user, lesson=lesson)
            data['success'] = True
            return render(request, 'main/lesson.html', data)

    return render(request, 'main/lesson.html', data)


def map(request):
    if not request.user.is_authenticated:
        return redirect('login')

    current_time = datetime.now().strftime('%H:%M')

    booked_lessons = Course.objects.filter(
        time__start__lte=current_time,
        time__end__gt=current_time,
        week_day=datetime.now().isoweekday()
    )

    booked_cabinet_ids = booked_lessons.values_list('cabinet__id', flat=True)

    free_cabinets = Cabinet.objects.exclude(id__in=booked_cabinet_ids)

    data = {
        'cabinets': [i.name.replace(' ', '') for i in free_cabinets]
    }

    return render(request, 'main/map.html', data)
