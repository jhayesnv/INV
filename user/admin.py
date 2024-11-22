from django.contrib import admin

from .models import (Position,
                     Employee)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
