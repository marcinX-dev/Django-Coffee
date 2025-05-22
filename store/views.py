from django.shortcuts import render, get_object_or_404
from .models import Coffee, Category
from cart.models import CartItem
from cart.views import _cart_id

def store(request, category_slug=None):
    categories = None
    coffees = None
    
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        coffees = Coffee.objects.filter(category=categories, is_available=True)
    else:
        coffees = Coffee.objects.all().filter(is_available=True)
    
    coffee_count = coffees.count()
    
    context = {
        'coffees': coffees,
        'coffee_count': coffee_count,
    }
    return render(request, 'store/store.html', context)

def coffee_detail(request, coffee_slug):
    try:
        single_coffee = Coffee.objects.get(slug=coffee_slug)
        # Sprawdź, czy kawa jest już w koszyku
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request),
            coffee=single_coffee
        ).exists()
    except Exception as e:
        raise e
        
    context = {
        'coffee': single_coffee,
        'in_cart': in_cart,
    }
    return render(request, 'store/coffee_detail.html', context)