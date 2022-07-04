from .views import login_custom, logout_custom,register_custom
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', register_custom, name='registercustom'),
    path('login/', login_custom, name='logincustom'),
    path('logout/', logout_custom, name='logoutcustom'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)