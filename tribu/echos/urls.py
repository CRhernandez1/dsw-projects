from django.urls import path, register_converter

import waves.views

from . import converters, views

app_name = 'echos'
register_converter(converters.EchoConverter, 'echo')

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.add_echo, name='add-echo'),
    path('<echo:echo>/', views.echo_detail, name='echo-detail'),
    path('<echo:echo>/waves/', views.echo_waves, name='echo-waves'),
    path('<echo:echo>/edit/', views.edit_echo, name='edit-echo'),
    path('<echo:echo>/delete/', views.delete_echo, name='delete-echo'),
    path('<echo:echo>/waves/add/', waves.views.add_wave, name='add-wave'),
]
