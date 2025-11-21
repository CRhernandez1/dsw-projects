from django.http import HttpResponse

from .models import Task


def check_exist_slug(view):
    def wrapper(request, task_slug, *args, **kwargs):
        try:
            request.task = Task.objects.get(slug=task_slug)
        except Task.DoesNotExist:
            return HttpResponse(f'La tarea con el slug {task_slug} no existe.')
        return view(request, task_slug, *args, **kwargs)

    return wrapper
