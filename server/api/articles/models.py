from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here.

class Sources(models.Model):

    json = JSONField()
    def __str__(self):
        return str(self.json)


class Article(models.Model):

    id = models.AutoField(primary_key=True)

    brand = models.CharField(max_length = 100, blank = False)
    
    title = models.CharField(max_length = 100, blank = False)

    url = models.CharField(max_length = 200, blank = False)
    clustered = models.BooleanField(default = False)
    
    added = models.DateTimeField(auto_now = True)

    cluster = models.ForeignKey("Cluster", null = True)

    json = JSONField()

    def __str__(self):
        return str(self.json)


class Cluster(models.Model):

    cluster_title = models.CharField(max_length = 100, blank = True)
    added = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(cluster_title)
