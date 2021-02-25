from django.db import models

from Management.models import Route


class Station(models.Model):
    """
    Model that represents a Route of transportation.
    """
    id = models.AutoField(primary_key=True)  # Identifier of the Route.
    name = models.CharField("Station name", max_length=100, blank=False, null=False)  # Route Name.
    route = models.ForeignKey(to=Route, on_delete=models.CASCADE, related_name='stations', related_query_name='station')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "route")
