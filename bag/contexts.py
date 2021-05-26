from django.conf import settings


def bag_contents(request):
    bag_items = []
    total = 0
    tour_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'tour_count': tour_count,
    }

    return context
