from django.db import models



class Route(models.Model):
    """
    Model that represents a Route of transportation.
    """
    id = models.AutoField(primary_key=True)  # Identifier of the Route.
    name = models.CharField("Route name", max_length=100, blank=False, null=False, unique=True)  # Route Name.

    def __str__(self):
        return self.name
