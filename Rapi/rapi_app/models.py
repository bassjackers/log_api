# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class LogData(models.Model):
    idx = models.BigAutoField(db_column='IDX', primary_key=True)  # Field name made lowercase.
    crtfckey = models.CharField(db_column='crtfcKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logdt = models.CharField(db_column='logDt', max_length=25, blank=True, null=True)  # Field name made lowercase.
    usese = models.CharField(db_column='useSe', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sysuser = models.CharField(db_column='sysUser', max_length=60, blank=True, null=True)  # Field name made lowercase.
    conectip = models.CharField(db_column='conectIp', max_length=30, blank=True, null=True)  # Field name made lowercase.
    datausgqty = models.IntegerField(db_column='dataUsgqty', blank=True, null=True)  # Field name made lowercase.
    send_yn = models.CharField(db_column='SEND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc_nm = models.CharField(db_column='PROC_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_SYS_LOG_SF'

    # def __str__(self):
    #     return self.conectip