from django.shortcuts import render

def coach(request):
    """function to render coach page"""
    
    return render(request, 'coaches/coach.html')
