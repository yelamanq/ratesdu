from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Max, Avg
from .forms import CommentsForm
from django.shortcuts import render, redirect
from .models import Comment, Rate, Rating, RateCache
import timeago, datetime, json
from django.contrib.auth.models import User

def teacher_profile(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    teacher = User.objects.get(pk=pk, is_staff=True)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save(user_id=request.user.pk, teacher_id=teacher.pk)
            return redirect('teacher_pk', pk=pk)

    form = CommentsForm()
    comments = Comment.objects.filter(teacher_id=pk, block=False).order_by('-date').values('user_id', 'user__username', 'content', 'date')
    print(comments.query)

    rate = Rate.objects.all()
    # print(rate.query)
    rate_list = []
    for i in rate:
        rate_cache_obj = RateCache.objects.filter(teacher_id=pk, rate_id=i.pk).first()
        overall_rating = rate_cache_obj.overall if rate_cache_obj else None

        rate_list.append({
            'rate_id': i.pk,
            'rate_text': i.rate_text,
            'overall': round(overall_rating, 1) if overall_rating is not None else 0,
        })
    data = {
        'rate': rate_list,
        'overall': round((RateCache.objects.filter(teacher_id=pk).aggregate(avg_overall=Avg('overall'))['avg_overall'] or 0), 1),
        'review_count': RateCache.objects.filter(teacher_id=pk).aggregate(Max('count'))['count__max'] or 0,
        'teacher': teacher,
        'form': form,
        'user': request.user,
        'comments': [
            {
                'user_id': i['user_id'],
                'username': i['user__username'],
                'is_super_user': request.user.is_superuser,
                'content': i['content'],
                # 'date': i.date.strftime('%Y-%m-%d %H:%M:%S')
                'date': timeago.format(datetime.datetime.strptime(i['date'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'), datetime.datetime.now())
            } for i in comments
        ]
    }

    return render(request, 'teacher/teacher.html', data)

def rate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        ratings = request.POST.get('ratings')
        teacher_id = request.POST.get('teacher_id')
        user_id = request.user.pk

        teacher = User.objects.filter(pk=teacher_id, is_staff=True)
        if not teacher.exists():
            return JsonResponse({'status': 'error'})


        ratings = json.loads(ratings)
        print(ratings)
        for i in ratings.items():
            i = i[1]
            rate = Rate.objects.filter(pk=i[0])
            if not rate.exists():
                return JsonResponse({'status': 'error'})
            if not str(i[2]).isnumeric():
                return JsonResponse({'status': 'error'})

            if int(i[2]) < 0 or int(i[2]) > 10:
                return JsonResponse({'status': 'error'})

            old_rate = Rating.objects.filter(user_id=user_id, teacher_id=teacher_id, rate_id=i[0])

            old_cache = RateCache.objects.filter(teacher_id=teacher_id, rate_id=i[0])
            if old_rate.exists():
                old_value = old_rate.first().rate_value
                if old_value != i[2]:
                    if old_cache.exists():
                        old_cache = old_cache.first()
                        old_cache.overall = (old_cache.overall * old_cache.count - old_value + i[2]) / old_cache.count
                        old_cache.save()
                    else:
                        RateCache.objects.create(teacher_id=teacher_id, rate_id=i[0], overall=i[2], count=1)
                    old_rate.update(rate_value=i[2])
            else:
                Rating.objects.create(user_id=user_id, teacher_id=teacher_id, rate_id=i[0], rate_value=i[2])
                if old_cache.exists():
                    old_cache = old_cache.first()
                    old_cache.overall = (old_cache.overall * old_cache.count + i[2]) / (old_cache.count + 1)
                    old_cache.count += 1
                    old_cache.save()
                else:
                    RateCache.objects.create(teacher_id=teacher_id, rate_id=i[0], overall=i[2], count=1)


        return JsonResponse({'status': 'ok'})

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    teachers_selected = User.objects.filter(is_staff=True).order_by('?')[:30]
    # print(teachers_selected.query)
    data = {
        'teachers': [
            {
                'teacher_id': i.pk,
                # 'gender': i.teacher_gender,
                'gender': 1,
                'avatar_id': i.pk % 19,
                'name': i.first_name + ' ' + i.last_name,
                'review_count': RateCache.objects.filter(teacher_id=i.pk).aggregate(Max('count'))['count__max'] or 0,
                'overall': (RateCache.objects.filter(teacher_id=i.pk).aggregate(avg_overall=Avg('overall'))['avg_overall'] or 0)/2
            } for i in teachers_selected
        ],
    }
    if request.user.is_authenticated:
        data['user'] = request.user
        return render(request, 'teacher/index.html', data)
    else:
        return redirect('login')

def teacher_search(request, query):
    if not request.user.is_authenticated:
        return redirect('login')

    teachers = User.objects.filter(username__icontains=query, is_staff=True)
    data = {
        'teachers': [
            {
                'teacher_id': i.pk,
                # 'gender': i.teacher_gender,
                'gender': 1,
                'avatar_id': i.pk % 19,
                'name': i.first_name + ' ' + i.last_name,
                'review_count': RateCache.objects.filter(teacher_id=i.pk).aggregate(Max('count'))[
                                    'count__max'] or 0,
                'overall': (RateCache.objects.filter(teacher_id=i.pk).aggregate(avg_overall=Avg('overall'))[
                                'avg_overall'] or 0) / 2
            } for i in teachers
        ],
    }

    return render(request, 'teacher/search.html', data)