from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Roopa',
        'title': 'Paneer Butter Masala',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    },

    {
        'author': 'Roopa',
        'title': 'Veg Manchuria',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    },

    {
        'author': 'Roopa',
        'title': 'Kofta Curry',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    }
]


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)


def about(request):
    return render(request, "recipes/about.html", {'title': 'about us page'})
