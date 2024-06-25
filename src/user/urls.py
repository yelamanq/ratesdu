from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.messages, name='message'),
    path('<int:pk>', views.user, name='user'),
    path('profile/delete_comment/<int:pk>', views.delete_comment, name='delete_comment'),
    path('logout/', views.logout_user, name='logout'),


    path('reset/', auth_views.PasswordResetView.as_view(template_name="reset/reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="reset/reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/reset_complete.html'), name='password_reset_complete'),
]

