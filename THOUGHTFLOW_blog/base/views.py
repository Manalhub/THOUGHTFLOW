from django.shortcuts import redirect, render, get_object_or_404
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
    recent_posts = Post.objects.all()[0:2]            

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
    filter_query = request.GET.get('search', '')
    query = Q(title__icontains=filter_query) | Q(author__username__icontains=filter_query) | Q(category__icontains=filter_query) | Q(body__icontains=filter_query)

    posts = Post.objects.filter(query)
    recent_posts = Post.objects.all()[:5]
    categ = Category.objects.all()

    context = {
        'posts': posts,
        'categ': categ,
        'recent_posts': recent_posts,
    }

    if request.user.is_authenticated:
        try:
            profile = Userprofile.objects.get(person=request.user)
            context['profile'] = profile
        except Userprofile.DoesNotExist:
            pass

    return render(request, 'index.html', context)

    
# CREATE POST
def create_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.user
        body = request.POST.get('body')
        category = request.POST.get('category')
        image = request.FILES.get('post-image', None)
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
    
    return render(request, 'create_post.html', {'categories': categories})

# READ post    
def read_post(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    similar_posts = Post.objects.filter(category=post.category)
    post_comments = Comment.objects.filter(comment_p=post)

    if request.method == 'POST':
        author = request.POST.get('name')
        body = request.POST.get('comment')
        signedup_user = request.user if request.user.is_authenticated else None

        new_comment = Comment(
            author=author,
            comment_p=post,
            body=body,
            signedup_user=signedup_user,
        )
        new_comment.save()

    return render(request, 'post.html', {
        'post': post,
        'similar_posts': similar_posts,
        'post_comments': post_comments,
    })

# Update post
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = POSTForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile', username=post.author.username, id=post.author.id)
    else:
        form = POSTForm(instance=post)
    
    return render(request, 'update_post.html', {
        'form': form,
        'post': post,
    })

# Delete post
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('profile', username=post.author.username, id=post.author.id)
    
    return render(request, 'delete.html', {
        'item': post,
        'type': 'post',
    })

# DELETE COMMENT
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        post_url = comment.comment_p.get_absolute_url()
        comment.delete()
        return redirect(post_url)
    
    return render(request, 'delete.html', {
        'item': comment,
        'type': 'comment',
    })

# Update Comment
def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'POST':
        form = COMForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        post_url = comment.comment_p.get_absolute_url()
        return redirect(post_url)
    else:
        form = COMForm(instance=comment)
    
    return render(request, 'update_comment.html', {
        'form': form,
        'comment': comment,
    })