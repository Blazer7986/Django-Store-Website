from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Products
from tags.models import TagItem

# Register your models here.
class TagInline(GenericTabularInline):
  autocomplete_fields = ['tag']
  model = TagItem
  
class CustomProductAdmin(ProductAdmin):
  inlines = [TagInline]
  
admin.site.unregister(Products)
admin.site.register(Products, CustomProductAdmin)