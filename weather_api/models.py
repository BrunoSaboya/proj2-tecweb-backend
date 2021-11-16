from django.db import models

class Favorits(models.Model):
    favorits = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.favorits)