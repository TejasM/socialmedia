from django.core.urlresolvers import reverse
from django.shortcuts import redirect

__author__ = 'tmehta'


def index(request):
    return redirect(reverse('dashboard:sample'))