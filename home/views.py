from django.shortcuts import render

# function to render home app
def index(request):
    """function to render home page"""
    return render(request, 'home/index.html')
