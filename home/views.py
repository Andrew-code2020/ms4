from django.shortcuts import render


def index(request):
    """function to render home page"""
    return render(request, 'home/index.html')
