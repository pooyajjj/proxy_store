from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm

admin.site.unregister(Group)



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_num', 'is_admin')
    list_filter = ('is_admin', )

    fieldsets = (
        ('Main', {'fields':('email', 'phone_num', 'first_name', 'password')}),
        ('permissions', {'fields':('is_active', 'is_admin', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields':('phone_num', 'email', 'first_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'first_name')
    ordering = ('first_name', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)