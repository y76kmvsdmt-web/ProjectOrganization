from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def location(request):
    return render(request, 'main/location.html')


def projects(request):
    return render(request, 'main/projects.html')


def services(request):
    return render(request, 'main/services.html')