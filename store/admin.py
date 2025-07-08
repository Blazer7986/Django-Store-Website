from django.contrib import admin
from . import models

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'unit_price', 'inventory_status']
  list_editable = ['unit_price'] # Unit price can be change on the admin side
  list_per_page = 10
  
  # Add a computed columns
  @admin.display(ordering='inventory')
  def inventoryStatus(self, product):
    if product.inventory < 10:
      return 'Low'
    return 'OK'
  
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