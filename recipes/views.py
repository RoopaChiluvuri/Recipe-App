from django.shortcuts import render, HttpResponse

recipes = [
    {
        'author': 'Dom',
        'title': 'Paneer Butter Masala',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    },

    {
        'author': 'Dom',
        'title': 'Veg Manchuria',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    },

    {
        'author': 'Dom',
        'title': 'Kofta Curry',
        'directions': 'combine all the ingredients',
        'date_posted': 'August 21, 2024'
    }
]


# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)


def about(request):
    return render(request, "recipes/about.html")
