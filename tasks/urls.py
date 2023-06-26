from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('not_completed/<int:task_id>/', views.mark_not_completed, name='mark_not_completed'),
    path('add/', views.add_task, name='add_task'),
]
