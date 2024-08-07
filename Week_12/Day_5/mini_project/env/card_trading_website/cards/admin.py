from django.contrib import admin

# Register your models here.
from .models import User, Card


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'amount_of_money', 'points')
    search_fields = ('username', 'email')


admin.site.register(User, UserAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = ('name_character', 'species', 'house', 'image_url', 'date_of_birth',
                    'patronus', 'price', 'xp_points', 'current_owner', 'previous_owner')
    search_fields = ('name_character', 'species', 'house')


admin.site.register(Card, CardAdmin)
