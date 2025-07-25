from django.db import models
# Allows generic relationships
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TagItemManger(models.Manager):
  def get_tags_for(self, obj_type, obj_id):
    content_type = ContentType.objects.get_for_model(obj_type)
    
    return TagItem.objects \
    .select_related('tags') \
    .filter(
      content_type = content_type,
      object_id = obj_id,
    )


# Create your models here.
class Tags(models.Model):
  label = models.CharField(max_length=255)
  
  def __str__(self):
    return self.label
  
class TagItem(models.Model):
  objects = TagItemManger()
  # What the tag is applied to what object
  tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
  # Type (product, video, article)
  # ID 
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveBigIntegerField()
  content_object = GenericForeignKey()
