from django.shortcuts import render, redirect, reverse, HttpResponse
from tours.models import Tour
from django.contrib import messages


def view_bag(request):
    """ A view to return the shopping bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, tour_id):
    """ Add a quantity of tours to the shopping bag """
    tour = Tour.objects.get(pk=tour_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if tour_id in list(bag.keys()):
        bag[tour_id] += quantity
    else:
        bag[tour_id] = quantity
        messages.error(request, f'Added {tour.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


# not working just yet
def adjust_bag(request, tour_id):
    """ Adjust the quantity of tours in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[tour_id] = quantity
    else:
        bag.pop(tour_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# not working just yet
def remove_from_bag(request, tour_id):
    """ Remove tour from the shopping bag """
    try:
        bag = request.session.get('bag', {})

        bag.pop(tour_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
