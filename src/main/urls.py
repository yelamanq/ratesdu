from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('read/', views.read, name='read'),
    path('lesson/<int:pk>', views.lesson, name='lesson'),
    path('lesson/', views.lesson, name='lesson_empty'),
    path('map/', views.map, name='map'),
]