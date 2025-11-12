from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Client, Product, Order, Stock

def index(request):
    return render(request, "index.html")

def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})


def products_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def orders_list(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})


def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, "stocks.html", {"stocks": stocks})
