from django.db import models


# Create your models here.

class Sources(models.Model):

    json = models.JSONField()
    __str__(self):
        return self.json


class Article(models.Model):

    id = models.AutoField(primary_key=True)

    brand = models.CharField(max_length = 50, blank = False)
    
    title = models.CharField(max_length = 50, blank = False)

    url = models.CharField(max_length = 100, blank = False)
    clustered = models.BooleanField(default = False)
    
    added = models.DateTimeField(auto_now = True)

    cluster = models.ForeignKey("Cluster", null = True)

    json = models.JSONField()

    def __str__(self):
        return self.json


class Cluster(models.Model):

    cluster_title = models.CharField(max_length = 50, blank = True)
    added = models.DateTimeField(auto_now = True)

    def __str__(self):
        return cluster_title
