import os
from forms import MomentForm
from forms import RegisterForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from models import Moment
from models import Register

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save()
            register.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = RegisterForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates','register.html'),
                  {'form':form})

def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates','moments_input.html'),
                  {'form':form})
def welcome(request):

    return HttpResponse('<h1>Welcome to my tiny twitter!</h1>')

def post_list(request):
    pString = ''
    list = Moment.objects.all()
    for i in list:
        pString += str(i.id) + ' ' + i.user_name + ' ' + i.kind + ' ' + i.content + '</br>'
    return HttpResponse(pString)
# Create your views here.
