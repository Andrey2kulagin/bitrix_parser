from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, RefreshInterval, BitrixAccountData, StopWords


class MyUserAdmin(UserAdmin):
    model = User
    list_display = (
        'username', 'email', "subscription", "activation_date", "subscription_days",
        "end_of_subscription")

    add_fieldsets = (*UserAdmin.add_fieldsets,
                     (
                         None,
                         {
                             'fields': (
                                 "subscription", "activation_date",
                                 "subscription_days",
                                 "end_of_subscription")}
                     ),
                     )

    fieldsets = ((*UserAdmin.fieldsets[0],),
                 (
                     None,
                     {
                         'fields': (
                             "subscription", "activation_date", "is_auth",
                             "subscription_days",
                             "end_of_subscription")}
                 ),
                 (*UserAdmin.fieldsets[3],)
                 )


admin.site.register(User, MyUserAdmin)
admin.site.register(RefreshInterval)
admin.site.register(BitrixAccountData)
admin.site.register(StopWords)