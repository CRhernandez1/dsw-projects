from django.urls import path

import waves.views

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.add_echo, name='add-echo'),
    path('<int:echo_id>/', views.echo_detail, name='echo-detail'),
    path('<int:echo_id>/waves/', views.echo_waves, name='echo-waves'),
    path('<int:echo_id>/edit/', views.edit_echo, name='edit-echo'),
    path('<int:echo_id>/delete/', views.delete_echo, name='delete-echo'),
    path('<int:echo_id>/waves/add/', waves.views.add_wave, name='add-wave'),
]
