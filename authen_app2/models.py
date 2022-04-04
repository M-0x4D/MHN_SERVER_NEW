from django.db import models

# Create your models here.

class HackerData(models.Model):
    hacker_ip = models.CharField(max_length=100)
    router_ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    web_bage = models.CharField(max_length=100)
    attach_time = models.TimeField(auto_now_add=True)
   # country = models.CharField(max_length=100)

class HakcerData2( HackerData,models.Model):
    country = models.CharField(max_length=100)


class HakcerData3(models.Model):
    hacker_ip = models.CharField(max_length=100)
    router_ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    web_bage = models.CharField(max_length=100)
    attach_time = models.TimeField(auto_now_add=True)
    country = models.CharField(max_length=100)


class HakcerData4(models.Model):
    hacker_ip = models.CharField(max_length=100)
    router_ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    web_bage = models.CharField(max_length=100)
    attach_time = models.TimeField(auto_now_add=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)