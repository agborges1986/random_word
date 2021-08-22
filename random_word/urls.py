from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('random/',views.random),
    path('success/',views.success),
    path('clear/',views.clear, name="clear"),
]
