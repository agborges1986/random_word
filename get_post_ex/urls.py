from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('forms',views.forms, name='forms'),
    path('info',views.info, name='info'),
    path('users',views.create_users, name='user'),
    path('success', views.success),
]
