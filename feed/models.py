from django.conf import settings
from django.db import models


class Priority(object):
    VERY_HIGH = 5
    HIGH = 4
    NORMAL = 3
    LOW = 2
    VERY_LOW = 1

    choices = (
        (VERY_HIGH, "Very High"),
        (HIGH, "High"),
        (NORMAL, "Normal"),
        (LOW, "Low"),
        (VERY_LOW, "Very Low"),
    )

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="Post")
    content = models.TextField(max_length=2000)
    published_at = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveIntegerField(choices=Priority.choices, default=Priority.NORMAL)

    def __unicode__(self):
        return self.content
