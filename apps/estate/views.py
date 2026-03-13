from django.shortcuts import render


def home(request):
    return render(request, "estate/index.html")

def about(request):
    return render(request, "about.html")

def property_grid(request):
    return render(request, "property-grid.html")

def blog_grid(request):
    return render(request, "blog-grid.html")

def contact(request):
    return render(request, "contact.html")

def agents(request):
    return render(request, "agents-grid.html")
