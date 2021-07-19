from django.contrib import admin
from django.db import models
from .models import Home, About, profile, category, Skills, Portfolio


# Home

admin.site.register(Home)


#About

class ProfileInline(admin.TabularInline):
    model = profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]    


#skills

class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]



#Portfolio

admin.site.register(Portfolio)

