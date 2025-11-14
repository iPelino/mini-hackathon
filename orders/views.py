from django.shortcuts import render
from django.views.generic import ListView

from orders.models import Order


# Create your views here.
class OrderList(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'


