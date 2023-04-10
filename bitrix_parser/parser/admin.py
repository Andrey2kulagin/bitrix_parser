from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', "subscription", "activation_date", "subscription_days",
        "end_of_subscription")

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password', 'email', 'first_name', 'last_name', "subscription", "activation_date",
                "subscription_days",
                "end_of_subscription")}
         ),
    )


admin.site.register(User, UserAdmin)
