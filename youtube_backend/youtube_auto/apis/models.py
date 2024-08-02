
from django.db import models

class Video(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    embed_url = models.URLField(max_length=500)
    published_at = models.DateTimeField()
    is_recent = models.BooleanField(default=True)
