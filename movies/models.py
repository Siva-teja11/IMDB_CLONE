from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    rating = models.IntegerField()
    urls = models.URLField(unique=True, null=True , blank=True)

    def __str__(self):
        return self.title

