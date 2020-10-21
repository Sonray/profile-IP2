from django.contrib import admin
from .models import Post, Comment, UserProfile

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal =("followers", "following",)

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile, admin_class=ProfileAdmin)