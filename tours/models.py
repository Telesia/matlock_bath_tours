from django.db import models


class Tour(models.Model):
    """ Model for Tours """
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """ Model migration design for reviews """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    review = models.TextField()

    class Meta:
        ordering = ['date_created']
