from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Gig(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_gigs', blank=True)

    def __str__(self):
        return self.title
