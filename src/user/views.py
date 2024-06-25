from django.shortcuts import render, redirect
from .forms import LoginForm, ResetForm, ChangePasswordForm
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import logout
from teacher.models import Comment

from main.models import Message

import datetime
import timeago

from main.models import Schedule


def login(request):
    if request.user.is_authenticated:
        return redirect('main')

    data = {
        'form': LoginForm(),
        'error': 0
    }

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                return redirect('main')
            else:
                data['error'] = 1
        else:
            data['form'] = form
            data['error'] = 1

    return render(request, 'login/login.html', data)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    comments = Comment.objects.filter(user_id=request.user.pk, block=False).order_by('-date')
    data = {
        'user': request.user,
        'form': ChangePasswordForm(request.user),
        'comments': [
            {
                'teacher_id': i.teacher_id,
                'comment_id': i.comment_id,
                'teacher_name': User.objects.get(pk=i.teacher_id, is_staff=True).username,
                'content': i.content,
            } for i in comments
        ]
    }

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        data['form'] = form

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            data['success'] = 1
    return render(request, 'profile/profile.html', data)

def delete_comment(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    comment = Comment.objects.get(comment_id=pk)
    if comment.user_id != request.user.pk:
        return redirect('profile')

    comment.block = True
    comment.save()
    return redirect('profile')

def logout_user(request):
    logout(request)
    return redirect('login')

def user(request, pk):
    if not request.user.is_authenticated and not request.uset.is_superuser:
        return redirect('login')

    comments = Comment.objects.filter(user_id=pk, block=False).order_by('-date')
    user = User.objects.get(pk=pk)
    data = {
        'user': user,
        'form': None,
        'comments': [
            {
                'teacher_id': i.teacher_id,
                'comment_id': i.comment_id,
                'teacher_name': User.objects.get(pk=i.teacher_id, is_staff=True).username,
                'content': i.content,
            } for i in comments
        ]
    }
    return render(request, 'profile/profile.html', data)

def messages(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user  # Assuming you have authentication enabled
    user_lessons = Schedule.objects.filter(user=user).values_list('lesson', flat=True)
    messages = Message.objects.filter(lesson__in=user_lessons).values('id', 'title', 'content',
                                                                                       'teacher__first_name',
                                                                                       'teacher__last_name', 'date')

    data = {
        "messages": [
            {
                'id': i['id'],
                'title': i['title'],
                'content': i['content'],
                'teacher': f"{i['teacher__first_name']} {i['teacher__last_name']}",
                "date": timeago.format(datetime.datetime.strptime(i['date'].strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'), datetime.datetime.now())
            } for i in messages
        ]
    }
    return render(request, 'profile/messages.html', data)