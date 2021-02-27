from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class SettingsManager(models.Manager):
    def get_settings(self):
        settings = self.get_queryset().first()

        if settings:
            return settings

        settings, __ = self.get_queryset().create()
        return settings

class Settings(models.Model):
    small_transporter_size = models.IntegerField(verbose_name=_('Small Transporter Size'), default= 1,validators=[MinValueValidator(1)] )
    medium_transporter_size = models.IntegerField(verbose_name=_('Medium Transporter Size'), default= 2,validators=[MinValueValidator(1)] )
    big_transporter_size = models.IntegerField(verbose_name=_('Big Transporter Size'), default= 3,validators=[MinValueValidator(1)] )

    objects = SettingsManager()
