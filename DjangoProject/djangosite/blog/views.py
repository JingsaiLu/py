from django.shortcuts import render
from django.http import HttpResponse
def blog_index(request):
    # return HttpResponse("Hello blog index")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)
# Create your views here.
