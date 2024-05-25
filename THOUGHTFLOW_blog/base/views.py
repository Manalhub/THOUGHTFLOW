from django.shortcuts import render
from profiles.models import Userprofile
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        profile = Userprofile.objects.get(person=request.user)
        posts = Post.objects.all()
        return render(request, 'index.html', {
            'posts': posts,
            'profile': profile,
        })
    else:
        posts = Post.objects.all()
        return render(request, 'index.html', {
            'posts': posts,
        })
    
def read_post(request, id, slug):
    
    try:
        post = Post.objects.get(id=id, slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    

    return render(request, 'post.html', {
              'post': post,    
    })