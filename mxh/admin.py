from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Notification, UserNotification, GroupChat, Task
from .models import Department, Post, Like

admin.site.register(Department)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(UserNotification)
admin.site.register(GroupChat)
admin.site.register(Task)


class CustomUserAdmin(UserAdmin):
    list_display = (
    'username', 'first_name', 'last_name', 'email', 'role', 'phone', 'birth_date', 'gender', 'department', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'birth_date', 'gender', 'department', 'avatar_url')
        }),
        ('Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'birth_date', 'gender', 'department', 'avatar_url', 'role')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Trường tìm kiếm trong Admin
    search_fields = ('username', 'first_name', 'last_name', 'email', 'department', 'role')

    # Các trường lọc
    list_filter = ('role', 'is_active', 'is_staff')


admin.site.register(User, CustomUserAdmin)
