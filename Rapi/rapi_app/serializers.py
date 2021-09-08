from django.core import serializers
from rest_framework import serializers
from .models import LogData

class LogDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogData
        fields = '__all__'
    crtfckey = serializers.CharField(max_length=100)  # Field name made lowercase.
    logdt = serializers.CharField(max_length=25)  # Field name made lowercase.
    usese = serializers.CharField(max_length=200)  # Field name made lowercase.
    sysuser = serializers.CharField(max_length=60)  # Field name made lowercase.
    conectip = serializers.CharField(max_length=30)  # Field name made lowercase.
    datausgqty = serializers.IntegerField()  # Field name made lowercase.
    send_yn = serializers.CharField(max_length=1)  # Field name made lowercase.
    proc_nm = serializers.CharField(max_length=50)  # Field name made lowercase.




    # ctkey = serializers.CharField(max_length=100)
    # logdate = serializers.CharField(max_length=25)
    # use = serializers.CharField(max_length=200)
    # user = serializers.CharField(max_length=60)
    # con_ip = serializers.CharField(max_length=30)