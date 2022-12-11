from django.db import models

# Create your models here.

class Order(models.Model):
    product_name = models.CharField(max_length=50)
    product_descrpition = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_brand = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f'{self.id}--{self.product_name}--{self.product_descrpition}'
    
