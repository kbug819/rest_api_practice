from django.db import models

class Drink(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)

  def __str__(self): # Will show as the name in the database
    return self.name 
  

  
class Customer(models.Model):
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  phone = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  location = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self): # Will show as the name in the database
    return self.first_name
  
class Tag(models.Model):
  name = models.CharField(max_length=200, null=True)

  def __str__(self): # Will show as the name in the database
    return self.name 
  
class Product(models.Model):
  CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),
            )
  name = models.CharField(max_length=200, null=True)
  price = models.FloatField(null=True)
  category = models.CharField(max_length=200, null=True, choices=CATEGORY)
  description = models.CharField(max_length=200, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  tags = models.ManyToManyField(Tag)

  def __str__(self): # Will show as the name in the database
    return self.name 
  

class Order(models.Model):
  STATUS = (
          ('pending', 'Pending'),
          ('out for delivery', 'Out for delivery'),
          ('Delivered', 'Delivered'),
          )
  customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
  product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  status = models.CharField(max_length=200, null=True, choices=STATUS)

###Practice build for project

class Market(models.Model):

  market_name = models.CharField(max_length=200, null=True)
  address = models.CharField(max_length=200, null=True)
  details = models.CharField(max_length=200, null=True)
  start_date = models.CharField(max_length=200, null=True)
  end_date = models.CharField(max_length=200, null=True)
  location = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self): # Will show as the name in the database
    return self.market_name 
  
class Vendor(models.Model):

  vendor_name = models.CharField(max_length=200, null=True)
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)
  location = models.CharField(max_length=200, null=True)
  market = models.ForeignKey(Market, null=True, on_delete= models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self): # Will show as the name in the database
    return self.vendor_name 
  
class Item(models.Model):

  item_name = models.CharField(max_length=200, null=True)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
  price = models.FloatField(null=True)
  size = models.CharField(max_length=200, null=True)
  quantity = models.IntegerField()
  available = models.BooleanField()
  description = models.CharField(max_length=200, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self): # Will show as the name in the database
    return self.item_name
  
class Preorder(models.Model):

  item_name = models.CharField(max_length=200, null=True)
  customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
  items = models.ManyToManyField(Item)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)






