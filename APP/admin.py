from django.contrib import admin
from .models import User,Project
# Register your models here.
admin.site.register(Project)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'email')