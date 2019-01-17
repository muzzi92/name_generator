from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "name_picker/index.html")

def entry(request):
    return render(request, "name_picker/entry.html")

def select(request):
    first_name = request.POST["first_name"]
    second_name = request.POST["second_name"]
    context = {
        "first_name": first_name,
        "second_name": second_name
    }
    return render(request, "name_picker/select.html", context)
