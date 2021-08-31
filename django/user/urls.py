from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import RegisterView

app_name = 'user'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


# for complect registration: log in/log out, password change, and password reset

# from django.contrib.auth import urls
# urlpatterns = [
#     path('', include(urls)),
# ]
