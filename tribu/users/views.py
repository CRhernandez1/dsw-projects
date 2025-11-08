from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Profile


@login_required
def user_list(request):
    profiles = Profile.objects.all()
    return render(request, 'users/user/list.html', {'profiles': profiles})
