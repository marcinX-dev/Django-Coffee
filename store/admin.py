from django.contrib import admin
from .models import Category, Coffee, Brewing

class BrewingInline(admin.TabularInline):
    model = Brewing
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'roast_date', 'is_available')
    list_filter = ('is_available', 'category', 'process')
    list_editable = ('price', 'stock', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description', 'region', 'flavor_profile')
    inlines = [BrewingInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Coffee, CoffeeAdmin)