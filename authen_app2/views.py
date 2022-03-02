from django.shortcuts import render
from rest_framework.response import Response
from .models import HackerData
from .serializer import Data_serializer
from rest_framework.decorators import api_view



# Create your views here.
def register_view(request):
    print('data')
    return render(request,'register.html')

def login_view(request):
    print('data')
    return render(request,'login.html')

    
@api_view(['POST' , 'GET'])
def show_data(request):
    hakerdata = HackerData.objects.all()
    h_data = Data_serializer(hakerdata,many=True).data
    return Response({'data':h_data})

def logout():
    pass