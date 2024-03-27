from django.contrib import admin
from .models import Category, Item

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent']
    search_fields = ['name', 'parent__name']
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_by', 'is_sold', 'is_approved']
    list_filter = ['is_approved', 'is_sold', 'category']
    search_fields = ['name', 'description', 'created_by__username']
    actions = ['approve_items']

    def approve_items(self, request, queryset):
        queryset.update(is_approved=True)
    approve_items.short_description = "Mark selected items as approved"
