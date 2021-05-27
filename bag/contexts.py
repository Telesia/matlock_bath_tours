from django.conf import settings
from django.shortcuts import get_object_or_404
from tours.models import Tour


def bag_contents(request):
    bag_items = []
    total = 0
    tour_count = 0
    bag = request.session.get('bag', {})

    for tour_id, quantity in bag.items():
        tour = get_object_or_404(Tour, pk=tour_id)
        total += quantity * tour.price
        tour_count += quantity
        bag_items.append({
            'tour_id': tour_id,
            'quantity': quantity,
            'tour': tour,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'tour_count': tour_count,
    }

    return context
