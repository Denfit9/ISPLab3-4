from django.db import models


class Category(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Tickets(models.Model):
    title = models.CharField('Name of ticket/coupon', max_length=80)
    description = models.TextField('Ticket description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
