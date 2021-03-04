from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    subject = models.CharField(max_length=500)
    email = models.EmailField()
    name = models.CharField(max_length=300)
    message = models.TextField()
