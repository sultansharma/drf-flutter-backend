
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from mysite.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homepage),
    path('user/', views.HelloView.as_view(), name='user'),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('register', views.Register.as_view(), name='register'),
    path('users', views.UsersList.as_view(), name='users')
   
]
