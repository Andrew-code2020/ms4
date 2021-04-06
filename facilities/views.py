from django.shortcuts import render

from .models import facility, FacilityCategory 


def free_weights(request):
    """function to render freeweights facilities page"""
    facilities = facility.objects.all()
    
    context = {
        'facilities': facilities,      
    }
    return render(request, 'facilities/freeweights.html', context)
