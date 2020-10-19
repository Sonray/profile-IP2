from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from .forms import NewImageForm,CommentForm,ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    images = Image.objects.all().order_by('-upload_date')
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request,"index.html",{"images":images,"form":form,"comments":comments})    

@login_required(login_url='accounts/login/')
def profile(request,username):
    current_user = request.user
    try:
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = current_user)
        images = Image.objects.filter(profile = profile)
        following = Profile.objects.filter(followers = user).count()
    
    except ObjectDoesNotExist:
        return redirect('edit_profile',current_user)

    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
    else:
        form = NewImageForm()
    return render(request,"profile.html",{"profile":profile, "images":images, "form":form,"following":following})



