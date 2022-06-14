from django.conf import settings
from django.db import models
from django.utils import timezone


class Journal(models.Model):
    title = models.CharField(max_length=100, blank = False)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add= True)


class Meta:
    ordering = ['date_created']
def __str__(self):
    return self. title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

