from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='orders')
    LIVE = 1
    DELETE = 0
    STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )
    CART_STAGE = 2
    ORDER_DELEVERED = 3
    ORDER_COMFIRMED = 4
    ORDER_CANCELLED = 5
    ORDER_PROCESSED = 6
    STATUS_CHOICE = ((CART_STAGE,'CART_STAGE'),
                    (ORDER_COMFIRMED,'ORDER_COMFIRMED'),
                    (ORDER_DELEVERED,'ORDER_DELEVERED'), 
                    (ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_CANCELLED,'ORDER_CANCELLED'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_status = models.IntegerField(choices=STATUS ,default=LIVE)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='added_carts')
    quantity = models.IntegerField()
    belongs_to = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')

