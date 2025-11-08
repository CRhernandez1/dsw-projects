from django.shortcuts import render

from .models import Profile


def user_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/user/list.html', {'profiles': profiles})
