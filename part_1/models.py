from django.db import models

# Create your models here.
class EndPoint(models.Model):
    url = models.TextField(default="")

    def __str__(self):
        return self.url

class StatusValue(models.Model):
    property_id = models.IntegerField()
    api_endpoint = models.ForeignKey(EndPoint, on_delete=models.CASCADE, null=True) 
    status = models.TextField(default="")
    value = models.TextField(default="")

    def __str__(self):
        return self.property_id

