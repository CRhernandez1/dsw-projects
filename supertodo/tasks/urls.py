from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('pending/', views.task_list_pending, name='task-list-pending'),
    path('completed/', views.task_list_completed, name='task-list-completed'),
]
