from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Cabinet
from main.models import Course, Schedule
from collections import defaultdict
from .models import CabinetStatusValue


# Create your views here.

def index(request):
    current_time = datetime.now().time()
    current_weekday = datetime.now().isoweekday()

    all_cabinets = Cabinet.objects.all()

    cabinets = []

    for cabinet in all_cabinets:
        if cabinet.name[:2] == 'VR' or cabinet.name[:2] == 'SH':
            continue
        if Course.objects.filter(cabinet=cabinet, time__start__lte=current_time, time__end__gte=current_time,
                                 week_day=current_weekday).exists():
            status = 1
        else:
            status = 0

        cabinets.append({
            'name': cabinet.name.replace(' ', ''),
            'status': status,
            'id': cabinet.id
        })
    data = {
        'cabinets': cabinets
    }

    return render(request, 'cabinet/index.html', data)


def cabinet(request, pk):
    current_time = datetime.now().time()
    current_weekday = datetime.now().isoweekday()


    cabinet = Cabinet.objects.get(id=pk)
    cabinet_schedule = Course.objects.filter(cabinet=pk).values('code', 'teacher__first_name', 'teacher__last_name',
                                                                'time__start', 'time__end', 'week_day', 'type',
                                                                'type_code')
    schedule_table = defaultdict(dict)
    day_mapping = {1: 'Mo', 2: 'Tu', 3: 'We', 4: 'Th', 5: 'Fr', 6: 'Sa'}
    for entry in cabinet_schedule:
        lesson_time = entry['time__start']
        week_day = entry['week_day']
        day_abbr = day_mapping[week_day]
        if lesson_time not in schedule_table:
            schedule_table[lesson_time] = defaultdict(list)
        schedule_table[lesson_time][day_abbr].append(entry)
    table_html = "<table><tbody><tr><td>Day/Hour</td>"
    for day_abbr in day_mapping.values():
        table_html += f"<td><span>{day_abbr}</span></td>"
    table_html += "</tr>"
    timeslots = [['09:00', '09:50'], ['10:00', '10:50'], ['11:00', '11:50'], ['12:00', '12:50'], ['13:00', '13:50'],
                 ['14:00', '14:50'], ['15:00', '15:50'], ['16:00', '16:50'], ['17:00', '17:50'], ['18:00', '18:50'], ['19:00', '19:50'], ['20:00', '20:50']]
    for start_time, end_time in timeslots:
        table_html += "<tr>"
        table_html += f"<td><span>{start_time}</span><br><span>{end_time}</span></td>"
        for day_abbr in day_mapping.values():
            day_lessons = schedule_table.get(start_time, {}).get(day_abbr, [])
            if day_lessons:
                lesson = day_lessons[0]  # Assuming only one lesson per time slot
                table_html += f"<td><a>{lesson['code']} [{lesson['type_code']}-{lesson['type']}]</a><span><br>{lesson['teacher__first_name']} {lesson['teacher__last_name'][0] if lesson['teacher__last_name'] else lesson['teacher__last_name']}.</span><br><span>{cabinet.name}</span></td>"
            else:
                table_html += "<td></td>"
        table_html += "</tr>"
    table_html += "</tbody></table>"

    tags = CabinetStatusValue.objects.filter(cabinet=pk).values('cabinet_status__caption', 'value')
    if Course.objects.filter(cabinet=cabinet, time__start__lte=current_time, time__end__gte=current_time,
                             week_day=current_weekday).exists():
        status = 1
    else:
        status = 0
    data = {
        "cabinet": cabinet,
        "schedule_table_html": table_html,
        "time": current_time.strftime("%H:%M"),
        "tags": [
            {
                'caption': i['cabinet_status__caption'],
                'value': i['value']
            } for i in tags
        ],
        "status": status
    }

    return render(request, 'cabinet/cabinet.html', data)


def search(request, query):
    if not request.user.is_authenticated:
        return redirect('login')

    current_time = datetime.now().time()
    current_weekday = datetime.now().isoweekday()

    all_cabinets = Cabinet.objects.filter(name__icontains=query)
    cabinets = []

    for cabinet in all_cabinets:
        if Course.objects.filter(cabinet=cabinet, time__start__lte=current_time, time__end__gte=current_time,
                                 week_day=current_weekday).exists():
            status = 1
        else:
            status = 0

        cabinets.append({
            'name': cabinet.name,
            'status': status,
            'id': cabinet.id
        })

    data = {
        'cabinets': cabinets
    }

    return render(request, 'cabinet/search.html', data)
