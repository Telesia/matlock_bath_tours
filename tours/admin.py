from django.contrib import admin
from .models import Tour


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Tour, TourAdmin)
