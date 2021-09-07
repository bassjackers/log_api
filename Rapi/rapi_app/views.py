from django.http import response
from django.shortcuts import render

from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import LogData
from .serialzers import LogDataSerializer
from .api import get_logdata

# Create your views here.

# @csrf_exempt
# def LogdataApi(request, id=0):
#     if request.method == "GET":
#         logdatas = LogData.objects.all()
#         logdatas_serializer = LogDataSerializer(logdatas, many=True)
#         return JsonResponse(logdatas_serializer.data,safe=False)
#     elif request.method == "POST":
#         logdata_dt = JSONParser().parse(request)
#         logdatas_serializer = LogDataSerializer(data=logdata_dt)
#         if logdatas_serializer.is_valid():
#             logdatas_serializer.save()
#             return JsonResponse("성공적으로 추가되었습니다.",safe=False)
#         return JsonResponse("추가 실패", safe=False)

class LogDataViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = LogDataSerializer
    queryset = LogData.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)



# @api_view(['GET'])
# def get_api(request):
#     queryset = LogData.objects.all()
#     print(queryset)
#     serializer = LogDataSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def post_api(request):
#     if request.method == 'GET':
#         return HttpResponse(status=200)
#     if request.method == 'POST':
#         serializer = LogDataSerializer(data = request.data, many=True)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data ,status=200)
#         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

