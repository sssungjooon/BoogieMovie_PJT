from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('<str:username>/', views.profile, name='profile'),
    # path('login/', views.login, name = 'login'),
    # path('logout/', views.logout, name='logout'),
    # path('<int:user_id>/', views.profile, name='profile'),
    path('login/', obtain_jwt_token), # login jwt 토큰 발급
]
