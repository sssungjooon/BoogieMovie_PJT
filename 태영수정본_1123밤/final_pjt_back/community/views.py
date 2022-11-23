from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Review, Comment
from movies.models import Movie
from .serializers import ReviewSerializer,ReviewListSerializer,CommentSerializer
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
from accounts.serializers import UserDetailSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http.response import JsonResponse

# JOON CODE
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        # reviews = Review.objects.all()
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data)

# Create your views here.
@api_view(['get'])
def reviews(request):
    try :
        page = int(request.GET.get('page'))
        all_reviews = Review.objects.all().prefetch_related('comment_set').prefetch_related('movie__genres').order_by('-created_at')
        p = Paginator(all_reviews, 8, allow_empty_first_page = True)
        reviews = p.page(page)

        #review = get_list_or_404(Review)
        #reviewserializer = ReviewListSerializer(review, many=True)    
        reviewserializer = ReviewListSerializer(data=reviews, many=True)
        print(reviewserializer.is_valid())
        return Response(reviewserializer.data)
    except Exception as e:
        # print(e)
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message' : '게시글 끝입니다'})

@api_view(['get'])
def review_detail(request,review_id):
    
    review = Review.objects.get(pk=review_id)
    review_list = [review]

    reviewserializer = ReviewSerializer(data=review_list, many=True)

    likedMovie_users=get_user_model().objects.filter(review__liked=True, review__movie=review.movie).distinct()
    userSerializer = UserDetailSerializer(data = likedMovie_users, many=True)

    loginUserSerializer = UserDetailSerializer(data=[request.user], many=True)
    print(reviewserializer.is_valid(), userSerializer.is_valid(),loginUserSerializer.is_valid())
    context={
        "0" : reviewserializer.data[0],
        "1" : userSerializer.data,
        "2" : loginUserSerializer.data,
    }

    return Response(context)

@api_view(['post'])
def review_craeted(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    # movie = Movie.objects.filter(id=movie_id)
    print(movie)
    serializer = ReviewSerializer(data =request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user = request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['delete'])
def review_delete(request,review_id):
    review = get_object_or_404(Review,pk=review_id)
    if request.user.pk == review.user.pk:
        review.delete()
        data ={
            'delete':f'데이터 {review_id}번 글이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['post'])
def comment_create(request,review_id):
    review = get_object_or_404(Review,pk=review_id)

    serializer = CommentSerializer(data =request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user = request.user)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['delete'])
def comment_delete(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if request.user.pk == comment.user.pk:
        comment.delete()
        data ={
            'delete':f'데이터 {comment_id}번 글이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['post'])
def like(request,review_id):
    review = get_object_or_404(Review,pk=review_id)
    user = request.user
    if review.user_id != user:
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            follow = False
        else:
            review.like_users.add(user)
            follow = True
        follow_status ={
            'follow':follow,
            'count':review.like_users.count(),
        }
        return JsonResponse(follow_status)

@api_view(['post'])
def comment_like(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    user = request.user
    if comment.user_id != user:
        if comment.like_users.filter(pk=user.pk).exists():
            comment.like_users.remove(user)
            follow = False
        else:
            comment.like_users.add(user)
            follow = True
        follow_status ={
            'follow':follow,
            'count':comment.like_users.count(),
        }
        return JsonResponse(follow_status)