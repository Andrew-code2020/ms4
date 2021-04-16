from django.contrib import admin

from django.contrib import admin

from .models import Order, OrderLineItem

# registering order and OrderLineItem model to Django admin


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',
                       'original_bag', 'stripe_pid')

    fields = ('order_number', 'date', 'user_profile', 'full_name',
              'email', 'phone_number', 'country',
              'town_or_city', 'street_address1',
              'street_address2', 'county', 'postcode',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
