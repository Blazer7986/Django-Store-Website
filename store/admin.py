from django.contrib import admin, messages
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from ..tags.models import TagItem

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

class OrderItemInline(admin.TabularInline):
  autocomplete_fields = ['product']
  model = models.OrderItems
  min_num = 1
  max_num = 10
  extra = 0
 
### Orders ####
@admin.register(models.Orders)
class OrderAdmin(admin.ModelAdmin):
  autocomplete_fields = ['cutomer']
  inlines = [OrderItemInline]
  list_display = ['placed_at', 'payment_status', 'cutomer']
  list_editable = ['payment_status']
  list_per_page = 50

class TagInline(GenericTabularInline):
  autocomplete_fields = ['tags']
  model = TagItem

### Products ####
@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
  autocomplete_fields = ['collection']
  prepopulated_fields = {
    'slug': ['title']
  }
  search_fields = ['title']
  # fields = ['title', 'slug'] # See title and slug are shown
  # excludes = ['promotions'] # Excludes promotions
  # readonly_fields = ['title'] # Cannot change title 
  actions = ['clear_inventory']
  inlines = [TagInline]
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
  
  @admin.action(description='Clear Inventory')
  def clear_inventory(self, request, queryset):
    updated_count = queryset.update(inventory=0)
    self.message_user(
      request,
      f'{updated_count} products were succesfully updated.',
      # messages.ERROR
    )
  
  def collection_title(self, product):
    return product.collection_set.title

### Customers ###
@admin.register(models.Customers)
class CustomerAdmin(admin.ModelAdmin):
  search_fields = ['id']
  list_display = ['first_name','last_name', 'email', 'membership']
  list_editable = ['membership']
  list_per_page = 50
  ordering = ['first_name', 'last_name']
  search_fields = ['first_name__istartswith', 'last_name__istartswith']
  
### Collection ###
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['title', 'product_count']
  search_fields = ['title']
  
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