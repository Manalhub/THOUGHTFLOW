from django.shortcuts import redirect, render
from django.db.models import Q
from base.forms import COMForm, POSTForm
from profiles.models import Userprofile
from django.http import Http404
from .models import Post, Category, Comment
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.text import slugify


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
    
# CREATE POST
def create_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.user
        body = request.POST.get('body')
        category = request.POST.get('category')
        try: 
            image = request.FILES['post-image']
        except MultiValueDictKeyError:
            image = None

        slug = slugify(title)

        post = Post(
            author=author,
            title=title,
            slug=slug,
            body=body,
            image=image,
            category=category,
        )
        post.save()
        return redirect('home')
    return render(request, 'create_post.html', {
        'categories':categories
    })

# READ post    
def read_post(request, id, slug):
    
    try:
        post = Post.objects.get(id=id, slug=slug)
        
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    similar_posts = Post.objects.filter(category=post.category)
    post_comments = Comment.objects.filter(comment_p=post)

    if request.method == 'POST':
        author = request.POST.get('name')
        body = request.POST.get('comment')
        
        if request.user.is_authenticated:
            new_comment = Comment(
                author=author,
                comment_p =post,
                body=body,
                signedup_user=request.user,
            )
        else:
            new_comment = Comment(
                author=author,
                comment_p=post,
                body=body,
                signedup_user=request.user,
            )
        new_comment.save()

    return render(request, 'post.html', {
        'post': post,
        'similar_posts': similar_posts,
        'post_comments' : post_comments,

    })

#Update post
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

#Delete post
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('profile', username=post.author.username,
        id=post.author.id)
    return render(request, 'delete.html', {
        'item':post,
        'type': 'post',
    })

#DELETE COMMENT
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        post = comment.comment_p
        post_url = post.get_absolute_url()
        comment.delete()
        return redirect(post_url)
    return render(request, 'delete.html',{
         'item':comment,
        'type': 'comment',
    })

# Update Comment
def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = COMForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        post = comment.comment_p
        post_url = post.get_absolute_url()
        return redirect(post_url)
    else:
       form = COMForm(instance=comment) 
    return render(request, 'update_comment.html',{
         'form':form,
        'comment': comment,
    })
