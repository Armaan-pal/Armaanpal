from django.shortcuts import render
from .models import Home, About, profile, category, Skills, Portfolio, Contact

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


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        Email = request.POST['Email']
        content = request.POST['content']
        contact = Contact(name=name, Email=Email, content=content)
        contact.save()
    return render(request,'index.html')


