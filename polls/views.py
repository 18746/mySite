from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<div style='color: red;'>123,32,234,35</div>")
# Create your views here.
