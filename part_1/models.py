from django.db import models

# Create your models here.

class StatusValue(models.Model):
    property_id = models.IntegerField()
    api_endpoint = models.ForeignKey(EndPoint, on_delete=models.CASCADE, null=True) 
    status = models.TextField(default="")
    value = models.IntegerField()

class Endpoint(models.Model):
    url = models.TextField(default="")
