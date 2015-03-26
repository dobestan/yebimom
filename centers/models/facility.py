from django.db import models
from centers.models.center import Center


class Facility(models.Model):
    center = models.ManyToManyField(Center, blank=True)

    name = models.CharField(max_length=40)

    def __unicode__(self):
        return unicode(self.name)
