from django.contrib import admin

from .models import Flat, Complain, Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flat.through
    extra = 3
    raw_id_fields = 'owner',


class FlatAdmin(admin.ModelAdmin):
    search_fields = 'town', 'address'
    readonly_fields = 'created_at',
    list_display = 'town', 'address', 'price', 'new_building', 'construction_year'
    list_editable = 'new_building',
    list_filter = 'new_building', 'has_balcony',
    raw_id_fields = 'liked_by', 'owners'
    inlines = OwnerInLine,


class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = 'flat', 'user'


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = 'flat',


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Owner, OwnerAdmin)
