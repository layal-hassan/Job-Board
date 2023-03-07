from django.contrib import admin
from .models import Category, Job, Apply

# Register your models here.
 
#Job  models
admin.site.register(Job)

#Category models
admin.site.register(Category)

admin.site.register(Apply)