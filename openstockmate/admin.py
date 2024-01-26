from django.contrib import admin
from .models import (
    CustomUser, Category, ComponentDocumentLink, Component,
    DocumentType, Document, LocationType, Location,
    Manufacturer, Package, PurchaseDetail, Purchase,
    Supplier, StockMovement, StockAlert, Feedback, Log
)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_verified', 'age', 'city', 'occupation')
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_staff', 'is_verified')

admin.site.register(CustomUser, CustomUserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent_id')
    search_fields = ('name',)
    list_filter = ('parent_id',)

admin.site.register(Category, CategoryAdmin)

class ComponentDocumentLinkAdmin(admin.ModelAdmin):
    list_display = ('document', 'component')
    search_fields = ('document__name', 'component__model')

admin.site.register(ComponentDocumentLink, ComponentDocumentLinkAdmin)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('model', 'description', 'manufacturer', 'category', 'package', 'location', 'stock', 'created_at', 'updated_at')
    search_fields = ('model',)
    list_filter = ('manufacturer', 'category', 'package', 'location')

admin.site.register(Component, ComponentAdmin)

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(DocumentType, DocumentTypeAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'document_type', 'document_path')
    search_fields = ('name', 'title', 'document_type__name')
    list_filter = ('document_type',)

admin.site.register(Document, DocumentAdmin)

class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(LocationType, LocationTypeAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_type', 'parent_id')
    search_fields = ('name',)
    list_filter = ('location_type', 'parent_id')

admin.site.register(Location, LocationAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Manufacturer, ManufacturerAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Package, PackageAdmin)

class PurchaseDetailAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'component', 'quantity', 'cost', 'total_cost')
    search_fields = ('purchase__date', 'component__model')
    list_filter = ('purchase',)

admin.site.register(PurchaseDetail, PurchaseDetailAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'supplier')
    search_fields = ('date', 'supplier__name')
    list_filter = ('supplier',)

admin.site.register(Purchase, PurchaseAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Supplier, SupplierAdmin)

class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('component', 'quantity', 'source_location', 'destination_location', 'created_at', 'updated_at')
    search_fields = ('component__model', 'source_location__name', 'destination_location__name')
    list_filter = ('source_location', 'destination_location')

admin.site.register(StockMovement, StockMovementAdmin)

class StockAlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'component', 'threshold')
    search_fields = ('user__email', 'component__model')
    list_filter = ('user', 'component')

admin.site.register(StockAlert, StockAlertAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)

admin.site.register(Feedback, FeedbackAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    search_fields = ('message',)
    list_filter = ('created_at',)

admin.site.register(Log, LogAdmin)
