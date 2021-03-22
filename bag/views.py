from django.shortcuts import render, redirect


def view_bag(request):
    """function to render shopping bag"""
    return render(request, 'bag/bag.html')



def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
            else:
                bag[item_id]['items_by_days'][days] = quantity
        else:
            bag[item_id] = {'items_by_days': {days: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
