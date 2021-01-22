from django.contrib import admin
from .models import Profile,Comment,Project,Rates

# Register your models here.

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Rates)
admin.site.register(Project)
