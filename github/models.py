from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
    gitlink = models.URLField(max_length=500)
    hostedlink = models.URLField(max_length=500, blank=True)

    objects = models.Manager()  # The default manager.

    def __str__(self):
        return self.title