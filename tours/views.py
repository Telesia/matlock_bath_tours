from audioop import reverse
from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Tour
from .forms import ReviewForm


def all_tours(request):
    """ A view to show all tours, including sorting and search queries"""

    tours = Tour.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please search for a walking tour!")
                return redirect(reverse('all_tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tours': tours,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'tours/tours.html', context)


def tour_detail(request, tour_id):
    """ A view to show individual tours"""

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/tour_detail.html', context)


def customer_review(request, tour_id):
    """ A view to submit a review of a tour to the db """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_detail')
    form = ReviewForm()
    context = {
        'form': form
    }

    return render(request, 'tours/tour_detail.html', context)
