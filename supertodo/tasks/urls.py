from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('pending/', views.task_list_pending, name='task-list-pending'),
    path('completed/', views.task_list_completed, name='task-list-completed'),
    path('add/', views.add_task, name='add-task'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
    path('<slug:task_slug>/delete/', views.delete_task, name='delete-task'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit-task'),
    path('<slug:task_slug>/toggle/', views.toggle_task, name='toggle-task'),
]
