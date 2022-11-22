import os

from django.shortcuts import render
from django.http import HttpResponse
from icrawler.builtin import GoogleImageCrawler


def index(request):
    dir = 'CDproject/static/CDproject/images'
    for file in os.scandir(dir):
        os.remove(file.path)

    type = 'cat and dog'
    if request.method == 'POST':
        if 'cat' in request.POST:
            type = 'cat'
        if 'dog' in request.POST:
            type = 'dog'

    google_crowler = GoogleImageCrawler(storage={'root_dir': dir})
    google_crowler.crawl(keyword=type, max_num=1)

    if os.path.exists(f'{dir}/000001.jpg'):
        url = '/CDproject/images/000001.jpg'
    else:
        url = '/CDproject/images/000001.png'

    return render(request, 'CDproject/index.html', {'url': url})
