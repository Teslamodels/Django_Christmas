from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUser, ChangeUser, CustomUser


class AdminUser(UserAdmin):
    add_form = CreateUser
    form = ChangeUser
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'middlename', 'birth_year', 'birth_month', 'birth_day', 'age']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', )}),
    )

admin.site.register(CustomUser, AdminUser)