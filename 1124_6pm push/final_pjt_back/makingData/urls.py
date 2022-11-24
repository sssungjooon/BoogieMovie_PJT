from django.urls import path
from . import views

app_name = 'makingData'

urlpatterns = [
    path('genre_data', views.genre_data),
    path('movie_data2', views.movie_data2),
    # path('dummyData', views.dummyData),
    # path('wakeUp', views.wakeUp)
]
