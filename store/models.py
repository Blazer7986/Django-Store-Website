from django.db import models

# Create your models here.
# Django will automatically insert an ID to classes
class Products(models.Model):
  # This how we normally make an id but its not needed in this case
  # sku = models.CharField(max_length=10, primary_key=True)
  title = models.CharField(max_length=255) # SQL varchar(255)
  description = models.TextField()
  # Don't use FloatFeild in this case # SQL float
  price = models.DecimalField(max_digits=6, decimal_places=2) 
  inventory = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)
  
class Cutomers(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=255)
  birth_day = models.DateField(null=True)
  