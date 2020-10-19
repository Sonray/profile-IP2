from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    ''' a model for Image posts '''
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['?'] #order randomly on feed

    def save_image(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_image(self):
        '''method to delete an image post instance '''
        self.delete()

    def update_caption(self, new_caption):
        ''' method to update an image's caption '''
        self.caption = new_caption
        self.save()
        
    @classmethod    
    def get_user_images(cls, user_id):
        ''' method to retrieve all images'''
        img = Image.objects.filter(profile=user_id).all()
        sort = sorted(img, key=lambda t: t.created_on)
        return sort
