from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.homepage_view, name='home'),                 #the homepage, defined in views.py
    path('messaging/', include('messaging.urls')),              #all urls belonging to messaging app is located in messaging urls.py
    path('auth/', include('django.contrib.auth.urls')),         #include auth urls under auth/ path
    path('auth/register/', views.signup_view, name='signup'),   #include custom registration
    path('admin/', admin.site.urls),                            #include standard admin site
]
