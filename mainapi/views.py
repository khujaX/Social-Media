from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from . import serializers
from .permissions import *


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (CanUpdateProfile,)


class FollowersList (generics.ListAPIView):
    serializer_class = serializers.FollowersSerializer

    def get_queryset(self):
        pk = self. kwargs['pk']
        return Follow.objects.filter (following_id=pk)


class FollowsList (generics.ListAPIView):
    serializer_class = serializers.FollowsSerializer

    def get_queryset(self):
        pk = self. kwargs['pk']
        return Follow.objects.filter (follower_id=pk)


class PostsList(generics.ListAPIView):
    serializer_class = serializers.PostViewSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostViewSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsPublisherOrReadOnly,)


class UserPostsList(generics.ListAPIView):
    serializer_class = serializers.UserPostsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Post.objects.filter(publisher=pk)


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)


class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsPublisherOrReadOnly,)


class PostComments(generics.ListAPIView):
    serializer_class = serializers.CommentsSerializer

    def get_queryset(self):
        pk = self. kwargs['pk']
        return Comment.objects.filter (comment_post=pk)


class LikeCreate(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsAuthenticated,)


class LikeDelete(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (IsLiker,)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsCommenter,)


class FollowCreate(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = (IsAuthenticated,)


class FollowDelete(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    permission_classes = (IsFollowerOrFollowing,)