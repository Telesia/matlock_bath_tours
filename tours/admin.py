from django.contrib import admin
from .models import Tour, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'review',
        'user',
        'tour',
        'created',
    )


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Tour, TourAdmin)
admin.site.register(Review, ReviewAdmin)
