from django.db import models


# Create your models here.



class Article(models.Model):

    source = models.CharField(max_length = 50, blank = False)
    
    original_title = models.CharField(max_length = 50, blank = False)

    article_text = models.TextField(blank = False)
    url = models.CharField(max_length = 100, blank = False)
    clustered = models.BooleanField(default = False)
    
    added = models.DateTimeField(auto_now = True)
    date = models.DateField(blank = False)

    cluster = models.ForeignKey("Cluster", null = True)



class Cluster(models.Model):

    cluster_title = models.CharField(max_length = 50, blank = True)
    added = models.DateTimeField(auto_now = True)

