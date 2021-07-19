#from _typeshed import Self
from django.db import models

# home section.

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=15)
    greetings_2 = models.CharField(max_length=15)
    picture = models.ImageField( upload_to='picture/')
    #save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


#about section

class About(models.Model):
    heading = models.CharField(max_length=50)
    carrer= models.CharField(max_length=20)
    descriotion= models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.carrer


class profile(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

#skills section

class category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skills'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


#portfolio section

class Portfolio (models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'