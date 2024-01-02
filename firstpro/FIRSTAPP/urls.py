from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_sigin, name='regist'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home_page, name='home'),
]
 