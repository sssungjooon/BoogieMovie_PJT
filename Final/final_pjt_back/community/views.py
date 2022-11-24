from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Review
from movies.models import Movie
from .serializers import ReviewSerializer,ReviewListSerializer
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
# from accounts.serializers import UserDetailSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from django.http.response import JsonResponse

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    # 전체 댓글 목록 조회_ 권한 없어도 가능 / GET
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    # 댓글 작성_ 권한 있어야 가능 / POST / 
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 게시글 수정, 삭제
@api_view(['DELETE', 'GET', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, review_pk)

    # 조회 기능
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 본인만 댓글 삭제 권한
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 본인만 댓글 수정 권한
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 본인만 댓글 삭제 권한
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 본인만 댓글 수정 권한
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



