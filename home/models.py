from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)
    slug = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500,blank = True)
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500)
    iamge = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    slug = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=500)
    comment = models.TextField()
    star = models.IntegerField(default = 5)
    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    twitter = models.URLField(max_length=100,blank=True)
    facebook = models.URLField(max_length=100,blank=True)
    linkedin = models.URLField(max_length=100,blank=True)
    insta = models.URLField(max_length=100,blank=True)
    youtube = models.URLField(max_length=100,blank=True)

    def __str__(self):
        return self.address



