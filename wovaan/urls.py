"""wovaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.template.context_processors import csrf
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

from wovaan.scrambler import scramble_cube

def hello(request):
    c = {}
    c.update(csrf(request))
    c['initialScramble'] = scramble_cube()
    return render_to_response('index.html', context=c)

def give_new_scramble(request):
    return HttpResponse(scramble_cube())

urlpatterns = [
    url(r'^updatescramble/?$', give_new_scramble),
    url(r'^/?$', hello),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
