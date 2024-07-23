from django.shortcuts import render, redirect
from django.http import HttpResponse
import redis

r = redis.Redis(host='redis', port=6379, db=0)


def index(request):
    return render(request, "app/index.html")


def clear(request):
    r.flushall()
    return redirect("/")
