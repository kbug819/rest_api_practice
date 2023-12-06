from django.core.management.base import BaseCommand
from ...models import Customer
from ...models import Order
from ...models import Product
from ...models import Tag

class Command(BaseCommand):
  help = 'Get the last customer'

  def handle(self, *args, **options):
    last_customer = Customer.objects.last()
    self.stdout.write(self.style.SUCCESS(f'Last Customer: {last_customer}'))

    order = Order.objects.first()
    customer_order = order.customer.name
    self.stdout.write(self.style.SUCCESS(f'customer_order: {customer_order}'))

    customer = Customer.objects.first().id
    orders = Order.objects.filter(customer=customer)
    self.stdout.write(self.style.SUCCESS(f'order: {orders}'))