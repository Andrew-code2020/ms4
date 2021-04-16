from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """function to render gym bag"""
    return render(request, 'bag/bag.html')


# add item to the gym bag
# code taken from Boutique Ado project and adapted to this project
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    days = None
    if 'product_days' in request.POST:
        days = request.POST['product_days']
    bag = request.session.get('bag', {})

    if days:
        if item_id in list(bag.keys()):
            if days in bag[item_id]['items_by_days'].keys():
                bag[item_id]['items_by_days'][days] += quantity
                messages.success(
                    request, f'Added day {days.upper()} {product.name} amount to {bag[item_id]["items_by_days"][days]}')
            else:
                bag[item_id]['items_by_days'][days] = quantity
                messages.success(
                    request, f'Added day {days.upper()} {bag[item_id]} to your bag')
        else:
            bag[item_id] = {'items_by_days': {days: quantity}}
            messages.success(
                request, f'Added day {days.upper()} to {product.name} in your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} total in {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


# adjust item in gym bag
# code taken from Boutique Ado project and adapted to this project
def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    days = None
    if 'product_days' in request.POST:
        days = request.POST['product_days']
    bag = request.session.get('bag', {})

    if days:
        if quantity > 0:
            bag[item_id]['items_by_days'][days] = quantity
            messages.success(
                request, f'Updated day {days.upper()} {product.name} amount to {bag[item_id]["items_by_days"][days]}')
        else:
            del bag[item_id]['items_by_days'][days]
            if not bag[item_id]['items_by_days']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed day option {days.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} total in {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

# remove item from gym bag
# code taken from Boutique Ado project and adapted to this project


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        days = None
        if 'product_days' in request.POST:
            size = request.POST['product_days']
        bag = request.session.get('bag', {})

        if days:
            del bag[item_id]['items_by_days'][size]
            if not bag[item_id]['items_by_days']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed day option {days.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
