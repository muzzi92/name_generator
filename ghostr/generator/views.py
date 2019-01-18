from django.http import HttpResponse
from django.shortcuts import render
from generator.models import Ghosts

def index(request):
    names = Ghosts().names
    context = { "names": names }
    return render(request, "generator/index.html", context)

def entry(request):
    return render(request, "generator/entry.html")

def select(request):
    first_name = request.POST["first_name"]
    second_name = request.POST["second_name"]
    context = {
        "first_name": first_name,
        "second_name": second_name
    }
    return render(request, "generator/select.html", context)
