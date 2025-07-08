from django.db import models
# Create your models here.
# Django will automatically insert an ID to classes

# One to Many Relationships
# Collection - Product
# Customer - Order
# Order - Item
# Cart - Item

# Many to Many Relationship
# Promotion - Product

class Promotion(models.Model):
  description = models.CharField(max_length=255)
  discount = models.FloatField()

class Collection(models.Model):
  title = models.CharField(max_length=255)
  featured_product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name='+')
  
  def __str__(self) -> str:
      return self.title

  class Meta:
    ordering = ['title']
  

class Products(models.Model):
  # This how we normally make an id but its not needed in this case
  # sku = models.CharField(max_length=10, primary_key=True)
  title = models.CharField(max_length=255) # SQL varchar(255)
  slug = models.SlugField()
  description = models.TextField()
  # Don't use FloatFeild in this case # SQL float
  unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
  inventory = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  # Many to Many Relationship
  promotions = models.ManyToManyField(Promotion)
  
  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering = ['title']


class Customers(models.Model):
  MEMBERSHIP_BRONZE = 'B'
  MEMBERSHIP_SLIVER = 'S'
  MEMBERSHIP_GOLD = 'G'
  
  MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_BRONZE, 'Bronze'),
    (MEMBERSHIP_SLIVER, 'Sliver'),
    (MEMBERSHIP_GOLD, 'Gold')
  ]
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
  # order_set
  
  def __str__(self) -> str:
    return self.first_name
  
  class Meta:
    ordering = ['first_name', 'last_name']


class Orders(models.Model):
  STATUS_PENDING = 'P'
  STATUS_COMPLETED = 'C'
  STATUS_FAILED = 'F'
  
  PAYMENT_STATUS_CHOICES = [
    (STATUS_PENDING, 'Pending'),
    (STATUS_COMPLETED, 'Completed'),
    (STATUS_FAILED, 'Failed')
  ]
  placed_at = models.DateTimeField(auto_now_add=True)
  payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES)
  cutomer = models.ForeignKey(Customers, on_delete=models.PROTECT)

class OrderItems(models.Model):
  # orderitem_set
  order = models.ForeignKey(Orders, on_delete=models.PROTECT)
  product = models.ForeignKey(Products, on_delete=models.PROTECT)
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  zip = models.PositiveSmallIntegerField(null=True)
  # One to One Relationship
  # customer = models.OneToOneField(Cutomers, on_delete=models.CASCADE, primary_key=True)
  # One to Many Relationship
  customer = models.ForeignKey(Customers, on_delete=models.CASCADE)


class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField()
