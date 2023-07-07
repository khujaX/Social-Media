from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/users/<int:pk>', UserDetail.as_view()),
    path('api/v1/user/profile/<int:pk>', UserProfile.as_view()),
    path('api/v1/user/followers/<int:pk>', FollowersList.as_view()),
    path('api/v1/user/follows/<int:pk>', FollowsList.as_view()),
    path('api/v1/user/<int:pk>/posts', UserPostsList.as_view()),

    path('api/v1/posts', PostsList.as_view()),
    path('api/v1/post/<int:pk>', PostDetail.as_view()),
    path('api/v1/post/details/<int:pk>', PostDetails.as_view()),
    path('api/v1/post/create', PostCreate.as_view()),
    path('api/v1/post/update/<int:pk>', PostUpdate.as_view()),
    path('api/v1/post/<int:pk>/comments', PostComments.as_view()),

    path('api/v1/like/create', LikeCreate.as_view()),
    path('api/v1/like/delete/<int:pk>', LikeDelete.as_view()),

    path('api/v1/comment/create', CommentCreate.as_view()),
    path('api/v1/comment/delete', CommentDelete.as_view()),

    path('api/v1/follow/create', FollowCreate.as_view()),
    path('api/v1/follow/delete/<int:pk>', FollowDelete.as_view()),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)