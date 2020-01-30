from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('author' , related_name='articles', on_delete= models.CASCADE)
