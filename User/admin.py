from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, RiderProfile

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


class RiderProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'profile_picture', 'dateOfBirth', 'gender', 'contactNumber', 'NidNumber', 'Nationality', 'vehicleType', 'drivingLicense')

admin.site.register(RiderProfile, RiderProfileAdmin)


# @admin.register(Customer_review)
# class Customer_Review_Admin(admin.ModelAdmin):
#     list_display=['rider','order','review_message']
    
# @admin.register(Customer_History)
# class Customer_History_Admin(admin.ModelAdmin):
#     list_display=['customer','delivery_time']