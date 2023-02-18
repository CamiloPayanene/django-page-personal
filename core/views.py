from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/index.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    return render(request, "core/contact.html")

# Create your views here.
