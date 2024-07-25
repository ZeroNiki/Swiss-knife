import os

from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


from .operations.main import main
from .utils import spoti_url_validation

import redis

r = redis.Redis(host='redis', port=6379, db=0)

def spoti(request):
    data_list = []
    for k in r.keys("*"):
        data = r.get(k)
        data_list.append(data.decode("utf-8"))

    return render(request, "app/spoti.html", {"url": data_list})

@require_http_methods(['POST'])
def sptotilink(request):
    url_cache_name = 'urls'
    url_cache = r.get(url_cache_name)

    if url_cache:
        url = url_cache
    else:
        url = request.POST.get("link")
        if url:
            if spoti_url_validation(url):
                r.set(url_cache_name, url, ex=35)
            else:
                r.set(url_cache_name, "Please, send sptoify link", ex=5)

    return redirect("/spotiDownloads")

def spotiInstall(request):
    link = []
    for k in r.keys('*'):   
        data = r.get(k)
        link.append(main(data.decode("utf-8")))

    response = FileResponse(open(link[0], 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(link[0])}"'
    response['Content-Type'] = 'application/octet-stream'

    def file_iterator():
        with open(link[0], 'rb') as f:
            yield from f
        os.remove(link[0])

    response.streaming_content = file_iterator()

    return response
