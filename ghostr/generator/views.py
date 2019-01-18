from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from generator.models import Ghosts
from django.urls import reverse

def index(request):
    names = Ghosts().names
    context = { "names": names }
    return render(request, "generator/index.html", context)

def entry(request):
    return render(request, "generator/entry.html")

def select(request):
    first_name = request.POST["first_name"]
    second_name = request.POST["second_name"]
    ghost_names = Ghosts().random_three()
    context = {
        "first_name": first_name,
        "second_name": second_name,
        "ghost_names": ghost_names
    }
    return render(request, "generator/select.html", context)

def create(request):
    chosen_name = request.POST["ghost_name"]
    print(chosen_name)
    return HttpResponseRedirect(reverse("index"))
