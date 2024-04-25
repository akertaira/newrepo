from django.db import models


class News(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
