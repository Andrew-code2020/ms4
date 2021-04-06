from django.shortcuts import render
from django.db.models import Q
from .models import facility, FacilityCategory


def free_weights(request):
    """function to render freeweights facilities page"""
    facilities = facility.objects.all()
    #facilitycategories = None

    #if request.GET:
        #if 'facilitycategory' in request.GET:
            #facilities = facilities.filter(category__name__in=facilitycategories)
            #facilitycategories = FacilityCategory.objects.filter(
                #name__in=facilitycategories)

    context = {
        'facilities': facilities,
        #'facilitycategories': facilitycategories,
    }
    return render(request, 'facilities/freeweights.html', context)
