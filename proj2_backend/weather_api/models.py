from django.db import models


DESCRIPTIONS = (
    (0, "Sunny"),
    (1, "Rain"),
    (2, "Cloudy"),
    (4, "Snow")
)




class Description(models.Model):
    description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    created_on = models.DateTimeField(auto_now_add = True)
    temperature = models.FloatField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.created_on)