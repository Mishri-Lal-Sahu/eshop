from django.db import models
from .category import Category

class Product(models.Model):
   name=models.CharField(max_length=50)
   price =models.IntegerField(default=0)
   description =models.CharField(max_length=200,default='')
   image=models.ImageField(upload_to='product/upload')
   category =models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

   @staticmethod
   def get_product_by_id(ids):
      return Product.objects.filter(id__in=ids)

   @staticmethod

   def get_all_product():
      return Product.objects.all()

   @staticmethod

   def get_all_product_by_id(category_id):
      if category_id:
         return Product.objects.filter(category = category_id)
      else:
         return Product.objects.all()