from django.db import models
# Allows generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Tags(models.Model):
  label = models.CharField(max_length=255)
  
class TagItem(models.Model):
  # What the tag is applied to what object
  tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
  # Type (product, video, article)
  # ID 
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveBigIntegerField()
  content_object = GenericForeignKey()
