from django.contrib import admin
from . import models


@admin.register(models.Orders)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['placed_at', 'payment_status', 'cutomer']
  list_editable = ['payment_status']
  list_per_page = 50

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
  list_editable = ['unit_price'] # Unit price can be change on the admin side
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
  ordering = ['first_name', 'last_name']
  list_per_page = 50
  
# Register your models here.
admin.site.register(models.Collection)
# admin.site.register(models.Products, ProductAdmin)
#  admin.site.register(models.Customers)