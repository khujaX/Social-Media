from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="sm-user/%Y/%m/%d/", blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    media = models.ImageField(upload_to="sc-media/%Y/%m/%d/")
    publisher = models.ForeignKey(User, related_name='publisher', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, related_name='writer', on_delete=models.CASCADE)
    written_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.writer} 's    comment under    {self.comment_post} post"


class Follow(models.Model):
    following = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    # following - Кому подписываются!!!!!!

    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    # follower - Кто подписывается!!!!!!!!

    def __str__(self) -> str:
        return f"{self.follower} 's follow to {self.following}"


class Like(models.Model):
    like_post = models.ForeignKey(Post, related_name='like_post', on_delete=models.CASCADE)
    liker = models.ForeignKey(User, related_name='liker', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"