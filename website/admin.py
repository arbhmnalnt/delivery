from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields=['name']
admin.site.register(Department, DepartmentAdmin)

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nameAr', 'nameEn', 'tags', 'slug', 'details')
admin.site.register(Product, ProductAdmin)

class VariationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product', 'size', 'color', 'price', 'details')

admin.site.register(Variation,VariationAdmin)
