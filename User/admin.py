from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name', 'role', 'profile_image')
    list_filter = ('role',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'profile_image', 'address', 'gender')}),
        ('Permissions', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()  # Remove reference to `groups` and `user_permissions`

# Register the new UserModelAdmin
admin.site.register(User, UserModelAdmin)
