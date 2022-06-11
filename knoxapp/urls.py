from .views import RegisterAPIPOST, RegisterAPIGET,LoginAPIPOST,LoginAPIGET,LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views


urlpatterns = [
    path('register-form/', RegisterAPIGET.as_view(), name='register'),
    path('valida-register/', RegisterAPIPOST.as_view(), name='validaregister'),
    path('login-form/', LoginAPIGET.as_view(), name='login'),
    path('valida-form/', LoginAPIPOST.as_view(), name='login-valida'),
    path('logout/', LogoutView.as_view(), name='logoutknox'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)