from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from wovaan.scrambler import scramble_cube
from .models import Solve

def timer_view(request):
    c = {}
    c.update(csrf(request))
    c['initialScramble'] = scramble_cube()
    return render_to_response('index.html', context=c)

def give_new_scramble(request):
    return HttpResponse(scramble_cube())

def add_solve(request):
    cubetype = request.POST.get('cubetype')
    scramble = request.POST.get('scramble')
    duration = request.POST.get('duration')

    solve = Solve(cubetype=cubetype, scramble=scramble, duration=duration)
    solve.save()

    return HttpResponse()

