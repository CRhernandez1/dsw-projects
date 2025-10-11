from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
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


def add_task(request):
    if (form := AddTaskForm(request.POST or None)).is_valid():
        task = form.save(commit=False)
        task.slug = slugify(task.name)
        task.save()
        return redirect('tasks:task-list')
    return render(request, 'tasks/task/add.html', dict(form=form))


def task_detail(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)
    except Task.DoesNotExist:
        return HttpResponse(f'La tarea con el slug {task_slug} no existe!')
    return render(request, 'tasks/task/detail.html', {'task': task})


def delete_task(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)
    except Task.DoesNotExist:
        return HttpResponse(f'La tarea con el slug {task_slug} no existe!')
    task.delete()
    return redirect('tasks:task-list')


def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if (form := EditTaskForm(request.POST or None, instance=task)).is_valid():
        task = form.save(commit=False)
        task.slug = slugify(task)
        task.save()
        return redirect('tasks:task-detail', task_slug=task.slug)
    return render(request, 'tasks/task/add.html', dict(task=task, form=form))


def toggle_task(request, task_slug: str):
    try:
        task = Task.objects.get(slug=task_slug)
    except Task.DoesNotExist:
        return HttpResponse(f'La tarea con el slug {task_slug} no existe!')
    task.completed = not task.completed
    task.save()
    return redirect('tasks:task-list')
