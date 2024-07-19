from django.urls import path

from . import views

urlpatterns = [
    path("", views.spoti, name="index"),
    path("spotilink", views.sptotilink, name="spotilink"),
    path("spotiinstall", views.spotiInstall, name="spotiinstall")
]
