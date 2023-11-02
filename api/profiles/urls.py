from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from profiles.views import RegisterAPI, Logout, UpdateProfileView

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', obtain_auth_token, name='api_token_auth'),
    path('logout', Logout.as_view(), name='logout'),

    path('update', UpdateProfileView.as_view(), name='update_profile'),
]
