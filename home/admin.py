from django.contrib import admin
from .models import Product, Category

# Registered product and Category models to home app.
admin.site.register(Product)
admin.site.register(Category)