from django.db import models

from Management.models import City


class Soldier(models.Model):
    """
    Model that represents the Soldier.
    """
    identification_number = models.CharField("Soldier's ID", max_length=20, blank=False, null=False)  # Soldier's identification number.
    first_name = models.CharField("Soldier's first name", max_length=50)  # Soldier's first name.
    last_name = models.CharField("Soldier's last name", max_length=50)  # Soldier's last name.
    phone = models.CharField("Soldier's phone", max_length=20)  # Soldier's phone number.
    city = models.ForeignKey(to=City, on_delete= models.CASCADE, related_name='soldiers', related_query_name='soldier')  # Soldier's City.
    structure = models.CharField("Soldier's structure", max_length=255)  # Soldier's role Structure (category 1\category 2\category 3).
