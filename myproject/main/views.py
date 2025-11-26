from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Client, Product, Order, Stock, SpecialOffer, Promotion, LoyaltyMembership, LoyaltyReward
from .forms import (
    ClientForm, ProductForm, OrderForm, StockForm,
    SpecialOfferForm, PromotionForm, LoyaltyMembershipForm, LoyaltyRewardForm
)

# === HOME ===
def index(request):
    return render(request, "index.html")


# === CLIENTS ===
def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Клиент успешно добавлен!")
            return redirect("clients")
    else:
        form = ClientForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить клиента", "back": "clients"})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения клиента сохранены!")
            return redirect("clients")
    else:
        form = ClientForm(instance=client)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать клиента", "back": "clients"})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        messages.success(request, "Клиент удалён!")
        return redirect("clients")
    return render(request, "confirm_delete.html", {"object": client, "back": "clients"})


# === PRODUCTS ===
def products_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Продукт успешно добавлен!")
            return redirect("products")
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form": form, "title": "Добавить продукт"})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения продукта сохранены!")
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    return render(request, "product_form.html", {"form": form, "title": "Редактировать продукт"})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Продукт удалён!")
        return redirect("products")
    return render(request, "product_confirm_delete.html", {"product": product})


# === ORDERS ===
def orders_list(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заказ успешно создан!")
            return redirect("orders")
    else:
        form = OrderForm()
    return render(request, "form_template.html", {"form": form, "title": "Создать заказ", "back": "orders"})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения заказа сохранены!")
            return redirect("orders")
    else:
        form = OrderForm(instance=order)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать заказ", "back": "orders"})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        messages.success(request, "Заказ удалён!")
        return redirect("orders")
    return render(request, "confirm_delete.html", {"object": order, "back": "orders"})


# === STOCKS ===
def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, "stocks.html", {"stocks": stocks})

def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Остаток успешно добавлен!")
            return redirect("stocks")
    else:
        form = StockForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить остаток", "back": "stocks"})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения остатка сохранены!")
            return redirect("stocks")
    else:
        form = StockForm(instance=stock)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать остаток", "back": "stocks"})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        messages.success(request, "Остаток удалён!")
        return redirect("stocks")
    return render(request, "confirm_delete.html", {"object": stock, "back": "stocks"})


# === SPECIAL OFFERS ===
def specialoffers_list(request):
    offers = SpecialOffer.objects.all()
    return render(request, "specialoffers.html", {"offers": offers})

def specialoffer_create(request):
    if request.method == "POST":
        form = SpecialOfferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Спец предложение добавлено!")
            return redirect("specialoffers")
    else:
        form = SpecialOfferForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить спец предложение", "back": "specialoffers"})

def specialoffer_update(request, pk):
    offer = get_object_or_404(SpecialOffer, pk=pk)
    if request.method == "POST":
        form = SpecialOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request, "Спец предложение обновлено!")
            return redirect("specialoffers")
    else:
        form = SpecialOfferForm(instance=offer)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать спец предложение", "back": "specialoffers"})

def specialoffer_delete(request, pk):
    offer = get_object_or_404(SpecialOffer, pk=pk)
    if request.method == "POST":
        offer.delete()
        messages.success(request, "Спец предложение удалено!")
        return redirect("specialoffers")
    return render(request, "confirm_delete.html", {"object": offer, "back": "specialoffers"})


# === PROMOTIONS ===
def promotion_list(request):
    promotions = Promotion.objects.all().order_by('-priority', 'start_date')
    return render(request, 'promotions/list.html', {'promotions': promotions})

def promotion_add(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Продвижение успешно добавлено!")
            return redirect('promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'promotions/form.html', {'form': form, 'title': 'Добавить продвижение'})

def promotion_edit(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения успешно сохранены!")
            return redirect('promotion_list')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotions/form.html', {'form': form, 'title': 'Редактировать продвижение'})

def promotion_delete(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == 'POST':
        promotion.delete()
        messages.success(request, "Продвижение удалено.")
        return redirect('promotion_list')
    return render(request, 'promotions/delete_confirm.html', {'promotion': promotion})


# === LOYALTY MEMBERSHIPS ===
def loyalty_list(request):
    memberships = LoyaltyMembership.objects.all()
    return render(request, "loyalty/memberships.html", {"memberships": memberships})

def loyalty_create(request):
    if request.method == "POST":
        form = LoyaltyMembershipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Участник лояльности добавлен!")
            return redirect("loyalty_list")
    else:
        form = LoyaltyMembershipForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить участника лояльности", "back": "loyalty_list"})

def loyalty_update(request, pk):
    membership = get_object_or_404(LoyaltyMembership, pk=pk)
    if request.method == "POST":
        form = LoyaltyMembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения участника лояльности сохранены!")
            return redirect("loyalty_list")
    else:
        form = LoyaltyMembershipForm(instance=membership)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать участника лояльности", "back": "loyalty_list"})

def loyalty_delete(request, pk):
    membership = get_object_or_404(LoyaltyMembership, pk=pk)
    if request.method == "POST":
        membership.delete()
        messages.success(request, "Участник лояльности удалён!")
        return redirect("loyalty_list")
    return render(request, "confirm_delete.html", {"object": membership, "back": "loyalty_list"})


# === LOYALTY REWARDS ===
def loyalty_rewards_list(request):
    rewards = LoyaltyReward.objects.all()
    return render(request, "loyalty/rewards.html", {"rewards": rewards})

def loyalty_reward_create(request):
    if request.method == "POST":
        form = LoyaltyRewardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Награда добавлена!")
            return redirect("loyalty_rewards_list")
    else:
        form = LoyaltyRewardForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить награду", "back": "loyalty_rewards_list"})
