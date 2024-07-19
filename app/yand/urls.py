from django.urls import path

from . import views

urlpatterns = [
    path("", views.yand , name="index"),
    path("yandLink", views.yandlink , name="yandlink"),
    path("yandInstall", views.yandinstall, name="yandInstall"),
]
