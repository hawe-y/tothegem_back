from django.contrib import admin
from input.models import *

@admin.register(Found_input)
class FoundAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'contact', 'registered_date',)
    list_filter = ('registered_date',)
    search_fields = ('name', )

@admin.register(Lost_input)
class LostAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'contact', 'registered_date',)
    list_filter = ('registered_date',)
    search_fields = ('name',)

