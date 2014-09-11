from collections import defaultdict
from dashboard.models import TwitterEvent
from django.shortcuts import render

__author__ = 'tmehta'


def sample(request):
    events = TwitterEvent.objects.all().values_list('event_occurrence', flat=True)
    times = {}
    for i in range(0, 24):
        times[i] = 0
    for e in events:
        if e.hour in times:
            times[e.hour] += 1
    return render(request, 'dashboard/index.html', {'times': times})