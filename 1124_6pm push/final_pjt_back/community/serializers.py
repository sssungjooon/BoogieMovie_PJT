from rest_framework import serializers
from movies.serializers import MovieDetailSerializer
from accounts.serializers import UserDetailSerializer
from .models import Review
from .models import Comment

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta :
        model = Review
        fields = ('id', 'title', 'content', 'user', 'username')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )



# copy code

# class ReviewListSerializer(serializers.ModelSerializer):
#     # movie_set = MovieSerializer(many=True, read_only=True)    
#     # movie_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


#     class Meta:
#         model =Review
#         fields = "__all__"

# class CommentSerializer(serializers.ModelSerializer):
#     user = UserDetailSerializer(read_only=True)
#     class Meta : 
#         model = Comment
#         # fields = ('id','user','content','created_at')
#         fields = "__all__"
#         read_only_fields = ('review','like_users',)

# class ReviewSerializer(serializers.ModelSerializer):
#     user = UserDetailSerializer(read_only=True)
#     movie = MovieDetailSerializer(read_only=True)
#     comment_set = CommentSerializer(read_only=True,many=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

#     class Meta : 
#         model = Review
#         fields = "__all__"
#         # exclude = ('like_users','funny_users','helpful_users')
#         read_only_fields =('movie','user','like_users','funny_users','helpful_users')


# class ReviewListSerializer(serializers.ModelSerializer):
#     movie = MovieDetailSerializer(read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)


#     class Meta : 
#         model = Review
#         exclude =('user','like_users','funny_users','helpful_users')
#         # exclude = ('like_users','funny_users','helpful_users')
#         read_only_fields =('movie',)