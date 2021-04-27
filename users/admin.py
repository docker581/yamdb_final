from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'bio', 'last_name', 'first_name')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
