from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from echos.models import Echo

from .forms import AddWaveForm
from .models import Wave


@login_required
def add_wave(request, echo_id):
    echo = get_object_or_404(Echo, id=echo_id)

    if (form := AddWaveForm(request.POST or None)).is_valid():
        wave = form.save(commit=False)
        wave.user = request.user
        wave.echo = echo
        wave.save()
        messages.success(request, 'Wave added successfully')
        return redirect('echos:echo-detail', echo_id=echo.id)
    return render(
        request,
        'echos/echo/add_echo.html',
        dict(form=form, cancel_url=reverse('echos:echo-detail', args=[echo.id])),
    )


@login_required
def edit_wave(request, wave_id):
    wave = get_object_or_404(Wave, id=wave_id)

    if wave.user != request.user:
        return HttpResponseForbidden()

    if (form := AddWaveForm(request.POST or None, instance=wave)).is_valid():
        wave = form.save(commit=False)
        wave.save()
        messages.success(request, 'Wave updated successfully')
        return redirect('echos:echo-detail', echo_id=wave.echo.id)
    return render(
        request,
        'echos/echo/add_echo.html',
        dict(form=form, cancel_url=reverse('echos:echo-detail', args=[wave.echo.id])),
    )


@login_required
def delete_wave(request, wave_id):
    wave = get_object_or_404(Wave, id=wave_id)

    if wave.user != request.user:
        return HttpResponseForbidden()
    echo_id = wave.echo.id
    wave.delete()
    messages.success(request, 'Wave deleted successfully')
    return redirect('echos:echo-detail', echo_id=echo_id)
