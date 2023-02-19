from django.shortcuts import render, HttpResponse


def portada(request):
    return render(request, "core/portada.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")

# Create your views here.
