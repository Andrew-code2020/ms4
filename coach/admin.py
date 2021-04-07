from django.contrib import admin

from .models import Coach

# Register your models here.

class CoachAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'qualification',
            'role',
            'image',
            )

    ordering = ('name',)


admin.site.register(Coach, CoachAdmin)