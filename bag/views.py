from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
        messages.success(request, f'Updated {tour.name} quantity to {bag[tour_id]}')
    else:
        bag[tour_id] = quantity
        messages.success(request, f'Added {tour.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


# not working just yet & need to add toasts messages if get working
def adjust_bag(request, tour_id):
    """ Adjust the quantity of tours in the shopping bag """

    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[tour_id] = quantity
        messages.success(request, f'Updated {tour.name} quantity to {bag[tour_id]}')
    else:
        bag.pop(tour_id)
        messages.success(request, f'Removed {tour.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# not working just yet & need to add toasts messages if get working
def remove_from_bag(request, tour_id):
    """ Remove tour from the shopping bag """
    try:
        product = get_object_or_404(Tour, pk=tour_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[tour_id]['items_by_size'][size]
            if not bag[tour_id]['items_by_size']:
                bag.pop(tour_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(tour_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
