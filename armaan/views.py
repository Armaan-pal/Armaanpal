from django.shortcuts import render
from .models import Home, About, profile, category, Skills, Portfolio

# Create your views here.

def index (request):
    #home
    home = Home.objects.latest('updated')

    #about
    about = About.objects.latest('updated')
    Profiles =profile.objects.filter(about=about)

    #skils
    categories = category.objects.all()

    #portfolio
    portfolios = Portfolio.objects.all()


    context ={
        'home' : home,
        'about' : about,
        'profiles' : Profiles,
        'categories' : categories,
        'portfolios' : portfolios
    }
    return render(request, 'index.html', context)

