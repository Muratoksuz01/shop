from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

class Catagorys(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images")
    descriptions=models.TextField()
    status=models.BooleanField()
    

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    categories=models.ManyToManyField(Catagorys,blank=True)
    name=models.CharField(max_length=200)
    vendor=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")
    quantity=models.IntegerField()
    original_price=models.IntegerField()
    selling_price=models.IntegerField()
    description=models.TextField()
    status=models.BooleanField()

    slug=models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    def save(self,*args,**kwargs):#burada otomatik kayıt etmesi için bir fonsiyon yazıd merak edersen https://www.youtube.com/watch?v=pxz4iXz_OlQ&list=PLXuv2PShkuHzrqh-_ZYuDcHZcoZfeAnad&index=22 bakabilirsin 
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    

class Favourites(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        image=models.ImageField(upload_to="images")
        name=models.CharField(max_length=200)
        unit=models.IntegerField()
        def __str__(self):
            return self.name

class Carts(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        image=models.ImageField(upload_to="images")
        name=models.CharField(max_length=200)
        unit=models.IntegerField()
        quantity=models.IntegerField()
        amount=models.IntegerField()
