from django.shortcuts import render
from django.db.models import Q
from .models import facility, FacilityCategory

#facilties app display on template and logic for filtering

def free_weights(request):
    """function to render freeweights facilities page"""
    facilities = facility.objects.all()
    facilitycategories = None

    if request.GET:
        if 'facilitycategory' in request.GET:
            facilitycategories = request.GET['facilitycategory'].split(',')
            facilities = facilities.filter(category__name__in=facilitycategories)
            facilitycategories = FacilityCategory.objects.filter(
                name__in=facilitycategories)
        

    context = {
        'facilities': facilities,
        'facilitycategories': facilitycategories,
    }
    return render(request, 'facilities/freeweights.html', context)
