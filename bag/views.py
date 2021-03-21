from django.shortcuts import render


def view_bag(request):
    """function to render shopping bag"""
    return render(request, 'bag/bag.html')
