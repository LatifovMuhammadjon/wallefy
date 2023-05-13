from django.contrib import admin
from .models import Category, InCome, OutCome
# Register your models here.
admin.site.register(Category)
admin.site.register(InCome)
admin.site.register(OutCome)