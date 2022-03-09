from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer , Data_serializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login , logout
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from .models import HackerData , HakcerData3
from datetime import datetime


@api_view(['GET' , 'POST'])
def show_api(request):
    hakerdata = HakcerData3.objects.all()
    h_data = Data_serializer(hakerdata,many=True).data
    #print(h_data)
    return Response({'data':h_data })



#honeypot api
@api_view(['POST'])
def sever_api(request,format=None):
    ip_ = request.POST.get("client_ip" , "no_hacker_ip")
    print("[+]==================================================================================[+]")
    print(ip_)
    web_page_ = request.POST.get("honeybot_name" , "no_web_bage")
    router_ip_ = request.POST.get("router_ip" , "no_router_ip")#request.POST['router_ip']
    print("[+]==================================================================================[+]")
    print(router_ip_)
    country = request.POST.get("country" , "no_country")
    print("[+]==================================================================================[+]")
    print(country)
    port = request.POST.get("port" , "no_port")
    attack_time = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = attack_time.strftime("%d/%m/%Y %H:%M:%S")
    print("[+]==================================================================================[+]")
   # print(request.data)
    print("[+]==================================================================================[+]")
    form  = HakcerData3(hacker_ip = ip_,  router_ip=router_ip_ ,port = port ,web_bage = web_page_ , attach_time = dt_string , country=country)
    form.save()
    #data = MHN_serializer(form,many=True).data
    hakerdata3 = HakcerData3.objects.all()
   # print(HackerData)
    print("[+]==================================================================================[+]")
    s_data = Data_serializer(hakerdata3,many=True).data
    #print(s_data)
    return Response({'data':s_data})





# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
#@api_view(['POST'])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

   # @api_view(['POST'])
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        #hakerdata = HackerData.objects.all()
        #h_data = Data_serializer(hakerdata,many=True).data
        return Response({"message": 'success'})



