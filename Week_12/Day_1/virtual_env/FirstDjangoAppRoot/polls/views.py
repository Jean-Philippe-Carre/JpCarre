from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


# def index(request):
#     return HttpResponse("<h1>Hello world wide web!!<h1>")

def index(request):
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render({}, request))
