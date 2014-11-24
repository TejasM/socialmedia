from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

__author__ = 'tmehta'


def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('dashboard:main'))
    if request.method == "GET":
        return render(request, 'dashboard/login.html')
    else:
        return redirect('/')