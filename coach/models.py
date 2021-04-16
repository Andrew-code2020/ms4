from django.db import models

# Coach Model.


class Coach(models.Model):
    name = models.CharField(max_length=254)
    qualification = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
