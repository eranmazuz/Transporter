from django.db import models

from django.utils.translation import gettext_lazy as _


class Soldier(models.Model):
    """
    Model that represents the Soldier.
    """
    identification_number = models.CharField(verbose_name=_("Soldier's ID"),
                                             max_length=20, blank=False,
                                             null=False, unique=True)  # Soldier's identification number.
    first_name = models.CharField(verbose_name=_("Soldier's first name"), max_length=50)  # Soldier's first name.
    last_name = models.CharField(verbose_name=_("Soldier's last name"), max_length=50)  # Soldier's last name.
    phone = models.CharField(verbose_name=_("Soldier's phone"), max_length=20)  # Soldier's phone number.
    city = models.CharField(verbose_name=_("Soldier's city"), max_length=20)  # Soldier's City.
    structure = models.CharField(verbose_name=_("Soldier's structure"),
                                 max_length=255)  # Soldier's role Structure (category 1\category 2\category 3).
    station = models.ForeignKey(verbose_name=_("Soldier's station"),
                                to='Station', on_delete=models.CASCADE, related_name='soldiers',
                                related_query_name='soldier')  # Soldier's station

    transporter = models.ForeignKey(verbose_name=_("Soldier's Transportation"),
                                to='Transporter', on_delete=models.CASCADE, related_name='soldiers',
                                related_query_name='soldier', default=None, null=True)  # Soldier's ransportation

