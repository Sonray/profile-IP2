from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length = 150, blank=True)
    followers = models.ManyToManyField(User,related_name='followers', blank=True)

    def save_profile(self):
        self.save()

    def update_bio(self):
        self.bio = bio
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return str(self.user)

    @classmethod
    def search_user(cls, username):
        user = User.objects.get(username = username)
        return user


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True,related_name='post_likes')
    upload_date = models.DateTimeField(auto_now_add=True,null=True) 

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        images = cls.objects.all().order_by('-upload_date')
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, caption):
        self.image_caption = caption
        self.save()

class Comment(models.Model):
    comment = models.CharField(max_length=2200)
    image = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)