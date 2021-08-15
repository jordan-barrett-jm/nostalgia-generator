from django.db import models

# Create your models here.
class Show(models.Model):
    CATEGORY_CHOICES = (
    ('2000s', '2000s'),
    ('1990s', '1990s'),
    ('2010s', '2010s'),
    ('1980s', '1980s')
    )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    start_year = models.IntegerField()
    end_year = models.IntegerField()