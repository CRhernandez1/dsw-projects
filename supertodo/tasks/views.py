from django.shortcuts import render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks})


def task_list_pending(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'tasks/task/list.html', {'tasks': tasks})


def task_list_completed(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/task/list.html', {'tasks': tasks})
