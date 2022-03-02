from django.db import models

# Create your models here.

class HackerData(models.Model):
    hacker_ip = models.CharField(max_length=100)
    router_ip = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    web_bage = models.CharField(max_length=100)
    attach_time = models.TimeField(auto_now_add=True)


