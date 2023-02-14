from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="products")

    def __str__(self):
        return self.name


class details(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)



