from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

class InventoryFilter(admin.SimpleListFilter):
  title = 'Inventory'
  parameter_name = 'inventory'
  
  def lookups(self, request, model_admin):
    return [
      ('<10', 'Low')
    ]
  
  def queryset(self, request, queryset):
    if self.value() == '<10':
      queryset.filter(inventory__lt=10)
      

@admin.register(models.Orders)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['placed_at', 'payment_status', 'cutomer']
  list_editable = ['payment_status']
  list_per_page = 50

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
  list_editable = ['unit_price'] # Unit price can be change on the admin side
  list_filter = ['collection', 'last_updated', InventoryFilter]
  list_per_page = 10
  list_select_related = ['collection']
  
  # Add a computed columns
  @admin.display(ordering='inventory')
  def inventoryStatus(self, product):
    if product.inventory < 10:
      return 'Low'
    return 'OK'
  
  def collection_title(self, product):
    return product.collection_set.title
  
@admin.register(models.Customers)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name','last_name', 'email', 'membership']
  list_editable = ['membership']
  list_per_page = 50
  ordering = ['first_name', 'last_name']
  search_fields = ['first_name__istartswith', 'last_name__istartswith']
  
  
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['title', 'product_count']
  
  @admin.display(ordering='product_count')
  def product_count(self, collection):
    url = (reverse(
          'admin:store_product_changelist') 
          + '?'
          + urlencode({
            'collection_id': str(collection.id)
          }))
    return format_html('<a href="{}">{}</a>', url, collection.products_count)
    
  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      product_count = Count('product')
    )
  
# Register your models here.
# admin.site.register(models.Collection)
# admin.site.register(models.Products, ProductAdmin)
# admin.site.register(models.Customers)