from django.shortcuts import render
from .models import House


def all_houses(request):
    houses = House.objects.all()
    return render(request, "houses/houses.html", {"houses": houses})
