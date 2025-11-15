from django.urls import path, register_converter

from . import converters, views

register_converter(converters.UserConverter, 'user')


app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('@me/', views.my_user_detail, name='my-user-detail'),
    path('<user:user>/', views.user_detail, name='user-detail'),
    path('<user:user>/echos/', views.user_echos, name='user-echos'),
    path('<user:user>/edit/', views.edit_profile, name='edit-profile'),
]
