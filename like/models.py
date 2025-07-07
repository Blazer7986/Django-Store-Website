from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class LikeItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
#   contentType = models.ForeignKey(ContentType, on_delete=models.PROTECT)
#   object_id = models.PositiveIntegerField()
#   content_object = GenericForeignKey()