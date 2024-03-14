from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for pizzeria."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.order_by()
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and all it's entries."""
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.entry_set.order_by()
    context = {'pizza':pizza, 'entries': entries}
    return render(request, 'pizzas/pizzas.html', context)
