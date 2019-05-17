from django.db import models

# Create your models here.

class Star(models.Model):
    star_text = models.CharField(max_length=20)

    def __str__(self):
        return self.star_text


class Vote(models.Model):

    star = models.ForeignKey(Star, related_name='votes', on_delete=models.CASCADE)

    def __str__(self):
        return self.star.star_text