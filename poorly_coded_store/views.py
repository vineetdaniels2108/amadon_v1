from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def create_order(request):
    quantity_from_form = int(request.POST["quantity"])
    
    product = Product.objects.get(id = request.POST['id'])
    
    product_price = float(product.price)
    total_charge = quantity_from_form * product_price
    print("Charging credit card...")
    order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    order_id = order.id
    return redirect(f'/checkout/{order_id}')

def checkout(request, order_id):
    orders = Order.objects.all()
    
    order_current = Order.objects.get(id = order_id)
    
    total_charge = order_current.total_price
    
    current_order_quantity = order_current.quantity_ordered
    
    total_quantity = 0
    all_orders_charge = 0 
    
    for order in orders:
        order_quantity = order.quantity_ordered
        charge_per_order = order.total_price
        total_quantity += order_quantity
        all_orders_charge += charge_per_order
    
    context = {
        'order' : order,
        'total_charge' : total_charge,
        'total_quantity' : total_quantity,
        'all_orders_charge' : all_orders_charge,
        'current_order_quantity' : current_order_quantity
    }
    return render(request, 'checkout.html', context)