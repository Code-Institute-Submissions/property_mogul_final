from django.shortcuts import render
from .models import House
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def all_houses(request):
    houses = House.objects.all()
    return render(request, "houses/houses.html", {"houses": houses})
