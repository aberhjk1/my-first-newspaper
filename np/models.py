from django.db import models
from django.utils import timezone


SECTIONS = (('NZ', 'NZ'),
            ('International', 'International'),
            ('Tech', 'Tech'),
            ('Sports', 'Sports'),)

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    intro_text = models.TextField()
    full_text = models.TextField()
    section = models.CharField(max_length=30, choices=SECTIONS)
    image_url = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
