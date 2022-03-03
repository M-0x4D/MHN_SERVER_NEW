from authen_app.api import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .api import LoginAPI , sever_api , logout_api
from .views import register_view , login_view , show_data , logout_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #api links
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/system/', sever_api, name='sysapi'),
    #path('api/system/', logout_api, name='sysapi')

    #views links
    path('register', register_view, name='register_view'),
    path('login', login_view, name='login_view'),
    path('show', show_data, name='show_data'),
    path('logout' , logout_view , name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)