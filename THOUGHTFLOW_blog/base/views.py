from django.shortcuts import render
from django.db.models import Q
from profiles.models import Userprofile
from django.shortcuts import render
from django.http import Http404
from .models import Post, Category

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        filter_query = request.GET.get('search') if request.GET.get('search') != None else ''
        # Search Engine
        posts = Post.objects.filter(
            Q(title__icontains=filter_query) |
            Q(author__username__icontains=filter_query) |
            Q(category__icontains=filter_query) |
            Q(body__icontains=filter_query)            
        )

        profile = Userprofile.objects.get(person=request.user)
        categ = Category.objects.all()
        # posts = Post.objects.all()
        return render(request, 'index.html', {
            'posts': posts,
            'profile': profile,
        })
    else:
        filter_query = request.GET.get('search') if request.GET.get('search') != None else ''
        # Search Engine
        posts = Post.objects.filter(
            Q(title__icontains=filter_query) |
            Q(author__username__icontains=filter_query) |
            Q(category__icontains=filter_query) |
            Q(body__icontains=filter_query) 
            
        )
        # posts = Post.objects.all()
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