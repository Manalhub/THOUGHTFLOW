from django.shortcuts import redirect, render
from django.db.models import Q
from base.forms import POSTForm
from profiles.models import Userprofile
from django.http import Http404
from .models import Post, Category

# Create your views here.
# Homepage
def post_categories(request,category):
    posts = Post.objects.filter(category=category)            
    recent_posts = Post.objects.all()[0:5]            

    # profile = Userprofile.objects.get(person=request.user)
    categ = Category.objects.all()
    # posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
        'recent_posts': recent_posts,
        #'profile': profile,
        'categ' : categ,
        })



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

        recent_posts = Post.objects.all()[0:5]            
        profile = Userprofile.objects.get(person=request.user)
        categ = Category.objects.all()
        # posts = Post.objects.all()
        return render(request, 'index.html', {
            'posts': posts,
            'profile': profile,
            'categ' : categ,
            'recent_posts': recent_posts,
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
        categ = Category.objects.all()
        recent_posts = Post.objects.all()[0:5]
        
        # posts = Post.objects.all()
        return render(request, 'index.html', {
            'posts': posts,
            'recent_posts': recent_posts,
            'categ': categ,
        })
# read a post    
def read_post(request, id, slug):
    
    try:
        post = Post.objects.get(id=id, slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    

    return render(request, 'post.html', {
              'post': post,  
    })

#update post
def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = POSTForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=post.author.username,
            id=post.author.id)
    else:
        form = POSTForm(instance=post)
    return render(request, 'update_post.html', {
        'form':form,
        'post':post,
    })