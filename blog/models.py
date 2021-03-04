from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Logo(models.Model):
    title = models.CharField(max_length=300)
    pictures = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title