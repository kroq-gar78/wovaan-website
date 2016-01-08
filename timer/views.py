from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max, Avg, Min
import json

import re

from wovaan.scrambler import scramble_cube
from .models import Solve, Puzzle

def timer_view(request, puzzle="3x3x3"):
    if puzzle is None: puzzle = "3x3x3" # TODO: figure out why 'puzzle' keeps matching to nothing
    puzzle = puzzle.lower()
    if(re.match(r'^[-\w0-9]+$', puzzle) is None): return HttpResponseBadRequest("Invalid puzzle '%s'" % puzzle)

    c = {}
    c.update(csrf(request))

    scramble = ""
    # TODO: make class/enums for puzzles
    try:
        scramble = Puzzle.objects.get(pk=puzzle).getScramble()
    except:
        return HttpResponseBadRequest("Field 'puzzle' = '%s' unknown or not specified" % puzzle)
    c['initialScramble'] = scramble
    c['puzzle'] = puzzle

    return render_to_response('index.html', context=c)

def stats_view(request):
    c = {}
    c.update(csrf(request))
    c['timesList'] = Solve.objects.all()[::-1]

    stats = {}
    stats['bestFive'] = Solve.objects.all()[:5].aggregate(Min('duration'))['duration__min']
    stats['bestTwelve'] = Solve.objects.all()[:12].aggregate(Min('duration'))['duration__min']
    stats['bestHundred'] = Solve.objects.all()[:100].aggregate(Min('duration'))['duration__min']
    stats['worstFive'] = Solve.objects.all()[:5].aggregate(Max('duration'))['duration__max']
    stats['worstTwelve'] = Solve.objects.all()[:12].aggregate(Max('duration'))['duration__max']
    stats['worstHundred'] = Solve.objects.all()[:5].aggregate(Max('duration'))['duration__max']

    average = {}
    average['five'] = round(Solve.objects.all()[:5].aggregate(Avg('duration'))['duration__avg'],3)
    average['twelve'] = round(Solve.objects.all()[:12].aggregate(Avg('duration'))['duration__avg'],3)
    average['hundred'] = round(Solve.objects.all()[:100].aggregate(Avg('duration'))['duration__avg'],3)



    c['averages'] = average
    c['stats'] = stats

    return render_to_response('stats.html', context=c)


@require_POST
def give_new_scramble(request):
    puzzle = request.POST.get("puzzle", default="3x3x3")
    puzzle = puzzle.lower()
    scramble = ""
    # TODO: make class/enums for puzzles
    try:
        scramble = Puzzle.objects.get(pk=puzzle).getScramble()
    except:
        print(puzzle)
        return HttpResponseBadRequest("Field 'puzzle' = '%s' unknown or not specified" % puzzle)

    return HttpResponse(scramble)

@require_POST
def add_solve(request):
    puzzle = request.POST.get('puzzle')
    scramble = request.POST.get('scramble')
    duration = request.POST.get('duration')

    solve = Solve(puzzle=puzzle, scramble=scramble, duration=duration)
    solve.save()

    return HttpResponse()

@require_POST
def give_time_list(request):
    puzzle = request.POST.get('puzzle')
    timesList = Solve.objects.filter(puzzle=puzzle).order_by("-date")[:10]
    innerHTML = ""
    for solve in timesList:
        innerHTML = innerHTML + "<li>" + str(solve.duration) + "</li>"
    return HttpResponse(innerHTML)

def give_json_times_data(request):
    data = Solve.objects.all().order_by("date").values('date', 'duration', 'scramble', 'puzzle')
    return JsonResponse(list(data), safe=False)
