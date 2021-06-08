from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Request bag contents from session
    bag = request.session.get('bag', {})

    # If nothing in bag add an error message
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    # Create an instance of the OrderForm from forms.py
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
