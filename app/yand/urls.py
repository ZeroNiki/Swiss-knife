from django.urls import path

from . import views

urlpatterns = [
    path("", views.yand , name="index"),
]
