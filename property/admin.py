from django.contrib import admin

from .models import Flat, Complain


class FlatAdmin(admin.ModelAdmin):
    search_fields = 'town', 'address'
    readonly_fields = 'created_at',
    list_display = 'town', 'address', 'price', 'new_building', 'construction_year'
    list_editable = 'new_building',
    list_filter = 'new_building', 'has_balcony',


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = 'flat',


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)