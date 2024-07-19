import os

from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .operations.install import dw1080, dw720, dw360, mp3
from .operations.info import getinfo  
from .utils import youtube_url_validation

from redis import StrictRedis
import re

# r = redis.Redis(host='localhost', port=6379, db=0, , decode_responses=True)
r = StrictRedis(decode_responses=False)


def yt(request):
    data_list = []
    for k in r.keys("*"):
        data = r.get(k)
        if data.decode("utf-8") != "Please, send youtube link":
            data_list.append(getinfo(data.decode("utf-8")))
        else:
            data_list.append(data.decode("utf-8"))
         
    return render(request, "app/yt.html", {"url": data_list})


@require_http_methods(['POST'])
def ytlink(request):
    url_cache_name = 'urls'
    url_cache = r.get(url_cache_name)

    if url_cache:
        url = url_cache
    else:
        url = request.POST.get("link")
        if url:
            if youtube_url_validation(url):
                r.set(url_cache_name, url, ex=60)
            else:
                r.set(url_cache_name, "Please, send youtube link", ex=5)

    return redirect("/ytDownloads")


def highRes(request):
    link = []
    for k in r.keys('*'):   
        data = r.get(k)
        link.append(dw1080(data.decode("utf-8")))

    response = FileResponse(open(link[0], 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(link[0])}"'
    response['Content-Type'] = 'application/octet-stream'

    def file_iterator():
        with open(link[0], 'rb') as f:
            yield from f
        os.remove(link[0])

    response.streaming_content = file_iterator()

    return response





def middleRes(request):
    link = []
    for k in r.keys('*'):   
        data = r.get(k)
        link.append(dw720(data.decode("utf-8")))

    response = FileResponse(open(link[0], 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(link[0])}"'
    response['Content-Type'] = 'application/octet-stream'

    def file_iterator():
        with open(link[0], 'rb') as f:
            yield from f
        os.remove(link[0])

    response.streaming_content = file_iterator()

    return response




def lowRes(request):
    link = []
    for k in r.keys('*'):   
        data = r.get(k)
        link.append(dw360(data.decode("utf-8")))

    response = FileResponse(open(link[0], 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(link[0])}"'
    response['Content-Type'] = 'application/octet-stream'

    def file_iterator():
        with open(link[0], 'rb') as f:
            yield from f
        os.remove(link[0])

    response.streaming_content = file_iterator()

    return response




def audio(request):
    link = []
    for k in r.keys('*'):   
        data = r.get(k)
        link.append(mp3(data.decode("utf-8")))

    response = FileResponse(open(link[0], 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(link[0])}"'
    response['Content-Type'] = 'application/octet-stream'

    def file_iterator():
        with open(link[0], 'rb') as f:
            yield from f
        os.remove(link[0])

    response.streaming_content = file_iterator()

    return response

















