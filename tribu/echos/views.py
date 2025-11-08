from django.shortcuts import redirect, render

from .forms import AddEchoForm
from .models import Echo


def echo_list(request):
    echos = Echo.objects.all()
    return render(request, 'echos/echo/list.html', {'echos': echos, 'n_echos': echos.count()})


def add_echo(request):
    if (form := AddEchoForm(request.POST or None)).is_valid():
        echo = form.save(commit=False)
        echo.user = request.user
        echo.save()
        return redirect('echos:echo-list')
    return render(request, 'echos/echo/add_echo.html', dict(form=form))
