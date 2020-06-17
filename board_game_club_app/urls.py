from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('login_now', views.login_now),
    path('register', views.register),
    path('register_now', views.register_now),
    path('logout', views.logout),
    path('events', views.events),
    path('create_event', views.create_event),
    path('join_event/<id>', views.join_event),
    path('leave_event/<id>', views.leave_event),
    path('werewolf', views.werewolf),
    path('avalon', views.avalon),
    path('tools', views.tools),
    path('remove_player/<id>', views.remove_player),
    path('shuffle', views.shuffle),
    path('cancel', views.cancel)
]
