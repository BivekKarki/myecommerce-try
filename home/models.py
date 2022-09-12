from django.db import models

STATUS = (('active', 'Active'),('inactive','Inactive'),('','Default'))  #frst value is db field name and sec value is valus of db
STOCK = (('In Stock','In Stock'),('Out of stock','Out of stock'))
LABELS = (('special','special'),('','Non special'))

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=400,unique=True)
    image = models.TextField()

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=400, unique=True)
    image = models.TextField()
    labels = models.CharField(max_length=200,choices=LABELS)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=200, choices=STATUS, blank=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=400, default='product')
    price = models.IntegerField()
    discounted_price = models.IntegerField(blank=True,default=0)
    status = models.CharField(max_length=200, choices=STATUS)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    stock = models.CharField(max_length=100, choices=STOCK)
    image = models.TextField()
    labels = models.CharField(max_length=200, choices=LABELS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()
    rank = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS,blank=True)

    def __str__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()
    rank = models.IntegerField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField()
    contact_id = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.email
