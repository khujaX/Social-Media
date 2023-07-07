from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import *


class UserRepSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'first_name', 'last_name']

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    follows_count = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'avatar', 'followers_count', 'follows_count', 'posts_count']

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep

    def get_follows_count(self, obj):
        return obj.follower.count()

    def get_followers_count(self, obj):
        return obj.following.count()

    def get_posts_count(self, obj):
        return obj.publisher.count()



class PostViewSerializer(serializers.ModelSerializer):
    publisher = UserRepSerializer()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.like_post.count()

    def get_comments_count(self, obj):
        return obj.comment_post.count()


class PostSerializer(serializers.ModelSerializer):
    publisher = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Follow
        fields = '__all__'


class FollowersSerializer (serializers. ModelSerializer):
    follower = UserRepSerializer()

    class Meta:
        model = Follow
        fields = '__all__'


class FollowsSerializer (serializers. ModelSerializer):
    following = UserRepSerializer()

    class Meta:
        model = Follow
        fields = '__all__'


class UserPostsSerializer (serializers. ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'media', 'published_date']


class CommentsSerializer(serializers.ModelSerializer):
    writer = UserRepSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    liker = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = '__all__'