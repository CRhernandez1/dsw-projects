from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import AddWaveForm


@login_required
def add_wave(request, echo):
    if (form := AddWaveForm(request.POST or None)).is_valid():
        wave = form.save(commit=False)
        wave.user = request.user
        wave.echo = echo
        wave.save()
        messages.success(request, 'Wave added successfully')
        return redirect('echos:echo-detail', echo)
    return render(
        request,
        'waves/wave/form_waves.html',
        {
            'form': form,
            'cancel_url': echo.get_absolute_url(),
            'submit_text': 'Añadir',
        },
    )


@login_required
def edit_wave(request, wave):
    if wave.user != request.user:
        return HttpResponseForbidden()

    if (form := AddWaveForm(request.POST or None, instance=wave)).is_valid():
        wave = form.save(commit=False)
        wave.save()
        messages.success(request, 'Wave updated successfully')
        return redirect('echos:echo-detail', wave.echo)
    return render(
        request,
        'waves/wave/form_waves.html',
        {
            'form': form,
            'cancel_url': wave.echo.get_absolute_url(),
            'submit_text': 'Editar',
        },
    )


@login_required
def delete_wave(request, wave):
    if wave.user != request.user:
        return HttpResponseForbidden()
    echo_id = wave.echo
    wave.delete()
    messages.success(request, 'Wave deleted successfully')
    return redirect('echos:echo-detail', echo_id)
