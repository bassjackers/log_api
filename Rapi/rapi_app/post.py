from .views import LogDataViewSet
from .models import LogData
from .serializers import LogDataSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse, JsonResponse

import json, requests



@csrf_exempt
def LogdataApi(request):
    URL = ('http://localhost:8098/api/test/getTest')
    data = LogData.objects.all()
    res = requests.post(URL, data=data)