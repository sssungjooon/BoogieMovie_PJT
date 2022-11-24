from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.reviews, name ='reviews'),
    path('<int:movie_id>/review/',views.review_craeted, name='review_craeted'),
    path('review/<int:review_id>/delete/',views.review_delete, name='review_delete'),
    path('<int:review_id>/',views.review_detail, name='review_detail'),

    path('<int:review_id>/comment/',views.comment_create, name='comment_create'),
    path('comment/<int:comment_id>/delete/',views.comment_delete, name='comment_delete'),

    path('<int:review_id>/like/',views.like, name='like'),
    # path('<int:review_id>/funny/',views.funny, name='funny'),
    # path('<int:review_id>/helpful/',views.helpful, name='helpful'),
    path('<int:comment_id>/comment/like/',views.comment_like, name='comment_like')
] 
