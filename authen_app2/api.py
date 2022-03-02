from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer , Data_serializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from .models import HackerData
from datetime import datetime




#honeypot api
@api_view(['POST'])
def sever_api(request,format=None):
    ip_ = request.POST['client_ip']
    web_page_ = request.POST['honeybot_name']
    router_ip_ = '14.45.67.89'#request.POST['router_ip']
    attack_time = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = attack_time.strftime("%d/%m/%Y %H:%M:%S")
    print("[+]==================================================================================[+]")
   # print(request.data)
    print("[+]==================================================================================[+]")
    form  = HackerData(hacker_ip = ip_,  router_ip=router_ip_ ,port = 3333 ,web_bage = web_page_ , attach_time = dt_string)
    form.save()
    #data = MHN_serializer(form,many=True).data
    hakerdata = HackerData.objects.all()
   # print(HackerData)
    print("[+]==================================================================================[+]")
    s_data = Data_serializer(hakerdata,many=True).data
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
        hakerdata = HackerData.objects.all()
        h_data = Data_serializer(hakerdata,many=True).data
        return Response({"message": h_data})




