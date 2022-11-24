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
    path('upcoming', views.upcomming),
    path('actors/<int:actor_pk>', views.get_actor_info),
    path('genres/<int:genre_pk>', views.get_genre_info),
    # path('tournament', views.tournament),
    path('mypageMovie/<str:username>', views.mypageMovie)
]
