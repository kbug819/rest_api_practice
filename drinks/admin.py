from django.contrib import admin
# from .models import Drink
# from .models import Customer
# from .models import Product
# from .models import Order
from .models import *

admin.site.register(Drink)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Market)
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Preorder)