from django.contrib import admin
from myfiles.models import Portfolio,Category
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','owner','rasm1']
admin.site.register(Portfolio,AdminPortfolio)

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name',]
admin.site.register(Category,AdminCategory)