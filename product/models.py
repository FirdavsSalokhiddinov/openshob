from django.db import models

CATEGORY_CHOICES = [
   ('mobile', 'Mobile'),
   ('tablet', 'Tablet'),
   ('laptop', 'Laptop'),
   ('pc', 'PC'),
   ('accessory', 'Accessory'),
   ('tv', 'TV'),
   ('home appliance', 'Home Appliance'),
   ('console', 'Console'),
]

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES, default='mobile')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_src = models.ImageField(upload_to='products/')
    image_src1 = models.ImageField(upload_to='products/', null=True, blank=True)
    image_src2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image_src3 = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name