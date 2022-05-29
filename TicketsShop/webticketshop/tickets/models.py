from django.db import models


class Ticket(models.Model):
    title = models.CharField('Name of ticket/coupon', max_length=80)
    description = models.TextField('Ticket description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
