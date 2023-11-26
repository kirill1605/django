from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:orders')
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'form': form})

def order_update(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_update.html', {'form': form, 'order': order})

def order_delete(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:orders')
    return render(request, 'orders/order_delete.html', {'order': order})
