from django.contrib import admin
from app_user.models import User, EmailVerification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['name', 'username', 'email']


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'created']
    readonly_fields = ['created']
    search_fields = ['user__username', 'user__email']
