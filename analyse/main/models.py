from django.db import models


class Price(models.Model):
    name = models.CharField(default=None, max_length=1000)
    photo = models.CharField(default=None, max_length=2083)
    mvideo_price = models.IntegerField(default=0)
    eldorado_price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
