from django.shortcuts import render, redirect, get_object_or_404
from store.models import Coffee
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            coffee=coffee,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    
    return redirect('cart')

def remove_cart(request, coffee_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

def remove_cart_item(request, coffee_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item = CartItem.objects.get(coffee=coffee, cart=cart)
    cart_item.delete()
    
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.coffee.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    missing_amount = max(0, 150 - total)

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'missing_amount': missing_amount,
    }
    return render(request, 'cart/cart.html', context)
