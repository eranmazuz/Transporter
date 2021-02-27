from django.db import models
from django.utils.translation import gettext_lazy as _

class City(models.Model):
    """
    Model that represents the City.
    """
    id = models.AutoField(primary_key=True)  # Identifier of the City.
    name = models.CharField(_("City name"), max_length=100, blank=False, null=False, unique=True)  # City Name.
    station = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='cites', related_query_name='city')
