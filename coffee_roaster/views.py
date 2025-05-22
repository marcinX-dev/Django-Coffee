from django.shortcuts import render
from store.models import Coffee

def home(request):
    coffees = Coffee.objects.all().filter(is_available=True)[:6]  # Pokaż 6 najnowszych kaw
    
    context = {
        'coffees': coffees,
    }
    return render(request, 'home.html', context)