from django.shortcuts import render , redirect
from rest_framework.response import Response 
from .models import HackerData , HakcerData3 , HakcerData4
from .serializer import Data_serializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User




# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login_view')
    #print('data')
    return render(request,'register.html')


#@api_view(['GET'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('show_data')
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("show_data")
            # Redirect to a success page.
            ...
        else:
            print('data')
    return render(request,'login.html')


#@api_view(['POST' , 'GET'])
def show_data(request):
    if request.user.is_authenticated:
        hakerdata = HakcerData4.objects.all().order_by('id').reverse()
        h_data = Data_serializer(hakerdata,many=True).data
        return render(request,'show.html' ,{"data": h_data})
    else:
        return redirect('login_view')
    #return render(request,'show.html')
    




def logout_view(request):
    logout(request)
    return redirect('login_view')