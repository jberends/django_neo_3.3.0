from django.db import models


# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    text = models.TextField()
    status = models.CharField(choices=(('DRAFT', 'DRAFT'), ('FINAL', 'FINAL')), default='DRAFT', max_length=12)
