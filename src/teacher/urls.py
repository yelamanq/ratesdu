from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='teacher'),
    path('<int:pk>', views.teacher_profile, name='teacher_pk'),
    path('search/<str:query>', views.teacher_search, name='search'),
    path('rate', views.rate, name='rate'),
    path('search/', views.teacher_search, name='search_empty'),
]