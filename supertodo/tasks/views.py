from django.shortcuts import redirect, render
from django.utils.text import slugify

from .decorators import check_exist_slug
from .forms import AddTaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Todas las tareas'})


def task_list_pending(request):
    tasks = Task.objects.filter(completed=False)
    return render(
        request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Tareas pendientes'}
    )


def task_list_completed(request):
    tasks = Task.objects.filter(completed=True)
    return render(
        request, 'tasks/task/list.html', {'tasks': tasks, 'subtitle': 'Tareas completadas'}
    )


def add_task(request):
    if (form := AddTaskForm(request.POST or None)).is_valid():
        task = form.save(commit=False)
        task.slug = slugify(task.name)
        task.save()
        return redirect('tasks:task-list')
    return render(request, 'tasks/task/form.html', {'form': form, 'subtitle': 'Añadir tarea'})


@check_exist_slug
def task_detail(request, task_slug):
    return render(request, 'tasks/task/detail.html', {'task': request.task})


@check_exist_slug
def delete_task(request, task_slug):
    request.task.delete()
    return redirect('tasks:task-list')


@check_exist_slug
def edit_task(request, task_slug):
    if (form := AddTaskForm(request.POST or None, instance=request.task)).is_valid():
        task = form.save(commit=False)
        task.slug = slugify(task.name)
        task.save()
        return redirect('tasks:task-detail', task_slug=task.slug)
    return render(request, 'tasks/task/form.html', {'form': form, 'subtitle': 'Editar tarea'})


@check_exist_slug
def toggle_task(request, task_slug):
    request.task.completed = not request.task.completed
    request.task.save()
    return redirect('tasks:task-list')
