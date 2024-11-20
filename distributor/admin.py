from django.contrib import admin

from . import models as dm


@admin.register(dm.Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['name', 'active_sales_reps', 'order_dates']

    def active_sales_reps(self, obj):
        return ', '.join([sr.name for sr in obj.sales_reps.all()])


@admin.register(dm.SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email']
    search_fields = ['name', 'email']
