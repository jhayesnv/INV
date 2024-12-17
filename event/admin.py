from django.contrib import admin

from .models import (Event,
                     Guest,
                     Reservation)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
