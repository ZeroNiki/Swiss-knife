from django.urls import path

from . import views

urlpatterns = [
    path("", views.yt, name="index"),
    path("/ytlink", views.ytlink, name="ytlink"),
    path("/high", views.highRes, name="HighRes"),
    path("/middle", views.middleRes, name="MiddleRes"),
    path("/low", views.lowRes, name="LowRes"),
    path("/audio", views.audio, name="audio"),
]
