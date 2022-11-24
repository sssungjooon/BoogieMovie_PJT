from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('review/',views.review_list),
    path('review/<int:review_pk>/',views.review_detail),
]
