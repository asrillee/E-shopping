from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime
from django.conf import settings

# Create your models here.

def inventory_path(instance, filename):
    return '/'.join(['users', instance.user.username, filename])

class Inventory(models.Model):
    item_no = models.AutoField(primary_key=True)
    item_name = models.CharField(default='',max_length=1000,blank=True)
    item_category = models.CharField(default='',max_length=1000,blank=True)
    item_image = models.ImageField(upload_to=inventory_path)

# class Cart_Item_Instance(models.Model):
#     inventory = models.ForeignKey(Inventory)
#     cart = models.ForeignKey(Cart)

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_no = models.IntegerField(default='1',blank=True)
    inventory = models.ForeignKey(Inventory)
    quantity = models.IntegerField(default='1',blank=True)