from django.shortcuts import render


def free_weights(request):
    """function to render freeweights facilities page"""
    return render(request, 'facilities/freeweights.html')
