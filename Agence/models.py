from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class   Suite(models.Model):
    city = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128, unique=True)
    adress = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='suites/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
   
   
class   Room(models.Model):
    
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128, unique=True)
    adress = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rooms', blank=True, null=True)
    
    
   
    
