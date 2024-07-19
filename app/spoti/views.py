from django.shortcuts import render


def spoti(requests):
    return render(requests, "app/spoti.html")
