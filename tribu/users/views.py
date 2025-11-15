from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/user/list.html', {'profiles': profiles})


@login_required
def user_detail(request, user):
    echos = user.echos.all()
    show_more = echos.count() > 5
    echos = echos[:5]
    return render(
        request,
        'users/user/detail.html',
        {'user': user, 'echos': echos, 'show_more': show_more},
    )


@login_required
def user_echos(request, user):
    echos = user.echos.all()
    return render(
        request,
        'users/user/detail.html',
        {'echos': echos, 'user': user},
    )


@login_required
def my_user_detail(request):
    return redirect(request.user.profile)


@login_required
def edit_profile(request, user):
    if user != request.user:
        return HttpResponseForbidden()

    if (
        form := EditProfileForm(request.POST or None, request.FILES or None, instance=user.profile)
    ).is_valid():
        user = form.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('users:my-user-detail')
    return render(request, 'users/user/edit.html', {'form': form})
