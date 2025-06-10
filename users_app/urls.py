from django.urls import path
from . import views
from .views import Login,Logout

urlpatterns = [
    path('',views.register,name='register-page'),
    path('login/',Login.as_view(),name='login-page'),
    path('logout/',Logout.as_view(),name='logout-page'),
    path('profile/',views.profile,name='profile-page'),
    
] 

