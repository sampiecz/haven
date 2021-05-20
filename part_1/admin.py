from django.contrib import admin
from part_1.models import EndPoint, StatusValue 

# Register your models here.
admin.site.register([EndPoint, StatusValue])
