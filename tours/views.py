from audioop import reverse
from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Tour


def all_tours(request):
    """ A view to show all tours, including sorting and search queries"""

    tours = Tour.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please search for a walking tour!")
                return redirect(reverse('all_tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_terms': query,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    """ A view to show individual tours"""

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)
