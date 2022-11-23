from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:movie_pk>/', views.detail, name='detail'),
    # path('tournament', views.tournament, name='tournament'),
    path('', views.main),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('recommend', views.recommend),
    # path('tournament', views.tournament),
    path('mypageMovie/<str:username>', views.mypageMovie)
]
