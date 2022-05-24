# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# def index(request):
#     return HttpResponse("Hello world!")

# def index(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

from .models import Members

# def index(request):
#   mymembers = Members.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["firstname"]
#     output += " "
#   return HttpResponse(output)

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

