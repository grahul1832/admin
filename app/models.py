from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name= models.CharField (max_length=100,primary_key=True)


class WebPage(models.Model):
    topic_name= models.ForeignKey (Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Url= models.URLField(max_length=100)

class AccessRecords(models.Model):
    name =models.ForeignKey(WebPage,on_delete=models.CASCADE)
    Data =models.DateField(max_length=100)
    author= models.CharField(max_length=100)
