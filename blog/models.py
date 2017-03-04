from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ZipCode(models.Model):
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=64)
    statecode = models.CharField(max_length=2)
    statename = models.CharField(max_length=32)
    create_date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):

        return "%s, %s (%s)" % (self.city, self.statecode, self.zipcode)

    class Meta:

        ordering = ['zipcode']



