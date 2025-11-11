from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('@me/', views.my_user_detail, name='my-user-detail'),
    path('<username>/', views.user_detail, name='user-detail'),
    path('<username>/echos/', views.user_echos, name='user-echos'),
    path('<username>/edit/', views.edit_profile, name='edit-profile'),
]
