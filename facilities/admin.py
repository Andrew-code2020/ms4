from django.contrib import admin



from .models import FacilityCategory, facility


class FacilityAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'description',
        'rating',
        'testimonial',
        'image',
        )

    ordering = ('name',)

class FacilityCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name', 
        'name',
    )

admin.site.register(FacilityCategory, FacilityCategoryAdmin)
admin.site.register(facility, FacilityAdmin)

