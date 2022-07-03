from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flat.through
    extra = 3
    raw_id_fields = 'owner',


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = 'town', 'address'
    readonly_fields = 'created_at',
    list_display = 'town', 'address', 'price', 'new_building', 'construction_year'
    list_editable = 'new_building',
    list_filter = 'new_building', 'has_balcony',
    raw_id_fields = 'liked_by', 'owners'
    inlines = OwnerInLine,


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = 'flat', 'user'


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = 'flat',

