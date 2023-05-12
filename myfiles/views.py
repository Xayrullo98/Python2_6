from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def index(malumot):
    malumotlar = Portfolio.objects.all()
    return render(malumot,'index.html',{"portfolio":malumotlar})

def portfolio(malumot,id):
    data = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{"work":data})