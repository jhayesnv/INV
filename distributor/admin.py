from django.contrib import admin

from . import models as dm


@admin.register(dm.Distributor)
class DistributorAdmin(admin.ModelAdmin):
    pass


@admin.register(dm.SalesRepresentative)
class SalesRepresentativeAdmin(admin.ModelAdmin):
    pass
