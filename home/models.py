from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.subject}"


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=50)
    time = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.address1} {self.address2}"
