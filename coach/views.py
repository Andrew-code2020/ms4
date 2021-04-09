from django.shortcuts import render
from .models import Coach

# coach logic and return of view 

def coach(request):
    """function to render coaches on page"""
    coaches = Coach.objects.all()

    context = {
        'coaches':coaches,
    }
    return render(request, 'coaches/coach.html', context)



