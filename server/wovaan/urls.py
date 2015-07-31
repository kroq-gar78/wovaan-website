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
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from wovaan.scrambler import scramble_cube

def hello(request):
    return render_to_response('index.html')

# TODO: remove the CSRF exempt stuff (not /that/ necessary, but still)
@csrf_exempt
def give_new_scramble(request):
    return HttpResponse(scramble_cube())

urlpatterns = [
    url(r'^updatescramble/?$', give_new_scramble),
    url(r'^.*/?$', hello),
]
