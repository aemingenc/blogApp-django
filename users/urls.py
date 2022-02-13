from django.urls import path
from .views import register,user_logout,user_login,profile_update
urlpatterns = [
    path('register/', register, name='register' ),
    path('logout/', user_logout, name='logout' ),
    path('login/', user_login, name='user_login' ),
    
    path('profile/<int:id>', profile_update, name='profile'),
]