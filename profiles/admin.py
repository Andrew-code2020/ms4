from django.contrib import admin


from .models import UserProfile

# inspired by boutique ado mini project
# adapted for this project


class UserProfileAdmin(admin.ModelAdmin):

    fields = ('user', 'default_full_name',
              'default_email', 'default_phone_number',
              'default_town_or_city', 'default_street_address1',
              'default_county', 'default_street_address2',
              'default_country', 'default_postcode',)

    list_display = ('user', 'default_full_name',
                    'default_email', 'default_phone_number',
                    'default_town_or_city', 'default_street_address1',
                    'default_county', 'default_street_address2',
                    'default_country', 'default_postcode',)

    ordering = ('-default_full_name',)

# register Userprofile to Django


admin.site.register(UserProfile, UserProfileAdmin)
