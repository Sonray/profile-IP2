from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(upload_to = 'exchangergramMOMENT/',blank=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    image = models.ImageField(blank=False, upload_to = 'exchangergram/')
    name = models.CharField(max_length=144, blank=True, default="Post")
    caption = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    
    def __str__(self):
        return f"{self.name} - {self.caption}"

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment