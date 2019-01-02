from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from main.views import *
from users.views import *

urlpatterns = [
    path('main/', Main.as_view(), name = 'main'),
    path('admin/', admin.site.urls),

    path('main/register/', Register.as_view(), name = 'register'),
    path('main/login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('main/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('main/profile/', Profile.as_view(), name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
