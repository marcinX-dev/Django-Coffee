from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

class Coffee(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    
    # Cena i zapasy - kluczowe dla sklepu
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    # Kategoria (np. Espresso, Filter, Omniroast)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    # Core fields for specialty coffee
    flavor_profile = models.TextField(help_text="Np. Czarna porzeczka, daktyle, pomarańcza krwista")
    region = models.CharField(max_length=100)
    process = models.CharField(max_length=50, help_text="Np. Washed, Natural")
    roast_date = models.DateField(help_text="Data palenia")
    roast_profile = models.CharField(max_length=100, help_text="Np. Jasny, do metod alternatywnych")
    weight = models.CharField(max_length=20, help_text="Np. 250g")
    
    # System fields
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Coffees'
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('coffee_detail', args=[self.slug])

class Brewing(models.Model):
    """Model dla sugerowanych metod parzenia kawy"""
    BREWING_METHOD_CHOICES = [
        ('aeropress', 'AeroPress'),
        ('chemex', 'Chemex'),
        ('drip', 'Drip/Pour Over'),
        ('espresso', 'Espresso'),
        ('french_press', 'French Press'),
        ('moka_pot', 'Moka Pot'),
        ('siphon', 'Siphon'),
        ('v60', 'V60'),
        ('kalita', 'Kalita Wave'),
        ('other', 'Inna'),
    ]
    
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='brewing_methods')
    method = models.CharField(max_length=50, choices=BREWING_METHOD_CHOICES)
    grind_size = models.CharField(max_length=50, help_text="Np. Średnio drobny, 2.2 na EK43")
    ratio = models.CharField(max_length=20, help_text="Np. 1:15")
    recipe = models.TextField(blank=True, help_text="Przepis na parzenie")
    
    def __str__(self):
        return f"{self.coffee.name} - {self.get_method_display()}"