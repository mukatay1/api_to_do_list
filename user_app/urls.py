from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')

]
