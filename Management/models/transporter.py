from django.db import models

class Transporter(models.Model):
    SMALL_TRANSPORTER = 'S'
    MEDIUM_TRANSPORTER = 'M'
    LARGE_TRANSPORTER = 'L'
    TRANSPORTER_SIZE_CHOICES = [
        (SMALL_TRANSPORTER, 'Small'),
        (MEDIUM_TRANSPORTER, 'Medium'),
        (LARGE_TRANSPORTER, 'Large'),

    ]
    stations = models.ManyToManyField(to='Station',
                                      related_name='transporters',
                                      related_query_name='transporter',
                                      through='TransporterForCity')

    size = models.CharField(max_length=1,
                            choices=TRANSPORTER_SIZE_CHOICES,
                            blank=False,
                            null=False)

    number = models.IntegerField(blank=False,
                                 null=False)

    platform = models.IntegerField(blank=False,
                                   null=False,
                                   unique=True)

    soldiers = models.ForeignKey


class TransporterForCity(models.Model):
    transporter = models.ForeignKey('Transporter',
                                    on_delete=models.CASCADE)

    station = models.ForeignKey('Station',
                                on_delete=models.CASCADE)

    occupied_seats = models.IntegerField(default=0)
