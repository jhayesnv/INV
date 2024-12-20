from django.contrib import admin

from .models import (Event,
                     Guest,
                     Reservation)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time']
    sortable_by = ['date', 'time']
    ordering = ['-date']


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email']
    sortable_by = ['name']
    search_fields = ['name', 'phone_number', 'email']
    ordering = ['name']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest__name', 'date', 'time', 'party_size',
                    'guest__phone_number']
    list_filter = ['date']
    search_fields = ['guest__name', 'guest__phone_number']
    ordering = ['-date']
