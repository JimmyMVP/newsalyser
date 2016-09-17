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

    category = models.CharField(max_length = 50, null = True)

    top_taxonomy = models.CharField(max_length = 50, null = True)

    tags = ArrayField(models.CharField(max_length = 30), null = True)

    def __str__(self):
        return str(self.json)

    #Extracts top taxonomy and labels
    def extract_top_taxonomy(taxonomy):

        tags = []
        firstLabel = taxonomy[0]["label"].split("/")[1:]
        tags.extend(firstLabel[1:])
        if(len(taxonomy) >= 2):
            secondLabel = taxonomy[1]["label"].split("/")[1:]
            if(taxonomy[1]["confident"] == "yes"):
                tags.extend(secondLabel)


        _category = firstLabel[0]
        _tags = tags

    def save(**kwargs):

        extract_top_taxonomy(kwargs["json"]["taxonomy"])
        super.save(kwargs)



class Cluster(models.Model):

    cluster_title = models.CharField(max_length = 100, blank = True)
    added = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(cluster_title)
