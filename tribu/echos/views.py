from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import AddEchoForm
from .models import Echo


@login_required
def echo_list(request):
    echos = Echo.objects.all()
    return render(request, 'echos/echo/list.html', {'echos': echos, 'n_echos': echos.count()})


@login_required
def add_echo(request):
    if (form := AddEchoForm(request.POST or None)).is_valid():
        echo = form.save(commit=False)
        echo.user = request.user
        echo.save()
        messages.success(request, 'Echo added successfully')
        return redirect(echo)
    return render(
        request,
        'echos/echo/form_echos.html',
        {'form': form, 'cancel_url': reverse('echos:echo-list'), 'submit_text': 'Añadir'},
    )


@login_required
def echo_detail(request, echo):
    waves = echo.waves.all()
    show_more = waves.count() > 5
    waves = waves[:5]
    return render(
        request, 'echos/echo/detail.html', {'echo': echo, 'waves': waves, 'show_more': show_more}
    )


@login_required
def echo_waves(request, echo):
    waves = echo.waves.all()
    return render(request, 'echos/echo/detail.html', {'echo': echo, 'waves': waves})


@login_required
def edit_echo(request, echo):
    if echo.user != request.user:
        return HttpResponseForbidden()

    if (form := AddEchoForm(request.POST or None, instance=echo)).is_valid():
        echo = form.save()
        messages.success(request, 'Echo updated successfully')
        return redirect('echos:echo-detail', echo)

    return render(
        request,
        'echos/echo/form_echos.html',
        {
            'form': form,
            'cancel_url': echo.get_absolute_url(),
            'submit_text': 'Editar',
        },
    )


@login_required
def delete_echo(request, echo):
    if echo.user != request.user:
        return HttpResponseForbidden()

    echo.delete()
    messages.success(request, 'Echo deleted successfully')
    return redirect('echos:echo-list')
