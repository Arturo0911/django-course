"""Django admin class"""


# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Local imports
from users.models import Profile
# Register your models here.

# admin.site.register(Profile)
from django.contrib.auth.models import User
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    
    list_display = ("pk", "user", "phone_number", "website", "picture")
    list_display_links = ("pk", "user") # to access any feature by link
    list_editable = ("phone_number", "website", "picture") # edit this fields
    search_fields = (
        "user__username",
        "user__email",
        "user__firstname", 
        "user__lastname", 
        "user__phone_number"
    )

    # to filter in query
    list_filter = (
        "created", 
        "modified",
        "user__is_active",
        "user__is_staff"
    )

    fieldsets = (

        ("Profile", {
            "fields": ("user", "picture")
        }),
        ("Extra info", {
            "fields": (
                ("website", "phone_number"),
                ("biography")
            ), 
        }),
        ("Metadata", {
            "fields": (("created", "modified"),),
        })
    )

    # when you can access to this field,
    # can't be edit 
    readonly_fields = ("created", "modified") 

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff"
    )



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
