from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='cabinet'),
    path('<int:pk>', views.cabinet, name='cabinet'),
    path('search/<str:query>', views.search, name='search_cabinet'),
    path('search/', views.search, name='search_cabinet_empty'),
]