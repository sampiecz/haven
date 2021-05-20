from django.shortcuts import render
from django.http import HttpResponse
from .models import EndPoint, StatusValue 
import requests

from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, StatusValue):
            return str(obj)
        return super().default(obj)

# Helper function that should go somewhere else 
# for now it lives here 
def getResult(endpoint, propertyId):
    try:
        response = requests.get(endpoint.url, params={"propertyId": propertyId})
        status = response.json()["status"]
        value = response.json()["value"]

        statusValue = StatusValue(
            status=status,
            value=value, 
            property_id=propertyId,
            api_endpoint=endpoint
        )

        statusValue.save()
        return statusValue
    except Exception as e:
        print(e)
        return None


# View
def index(request, propertyId):
    if not propertyId:
        return HttpResponse(status=500)

    results = StatusValue.objects.none() 

    # try and call all api endpoints
    for endpoint in EndPoint.objects.all():
        result = getResult(endpoint, propertyId)
        if result != None:
            results |= StatusValue.objects.filter(pk=result.pk)

    return HttpResponse(
        serialize('json', results, cls=LazyEncoder), 
        content_type='application/json'
    )

