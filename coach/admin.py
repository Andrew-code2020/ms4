from django.contrib import admin

from .models import Coach

# Registering coach model to the admin.


class CoachAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'qualification',
            'role',
            'image',
            )

    ordering = ('name',)


admin.site.register(Coach, CoachAdmin)
