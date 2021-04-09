from django import template

# to calculate subtotal in bag
# for each line item
# code taken from Boutique Ado project and adapted to this project

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity