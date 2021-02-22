from django.db import models



class City(models.Model):
    """
    Model that represents the City.
    """
    id = models.AutoField(primary_key=True)  # Identifier of the City.
    name = models.CharField("City name", max_length=100, blank=False, null=False)  # City Name.
