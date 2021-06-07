from django.db import models


class Talk(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60, default=None)
    last_name = models.CharField(max_length=60, default=None)
    speaker = models.CharField(max_length=60, default=None)
    venue = models.CharField(max_length=60, default=None)
    duration = models.DecimalField(max_digits=4, decimal_places=2)

    def __int__(self):
        return self.id
