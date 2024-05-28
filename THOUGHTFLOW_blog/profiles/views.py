from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import UserPForm
from base.models import Post
from .models import Userprofile
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required

# View for user login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')

# View for user logout
def user_logout(request):
    logout(request)
    return redirect('home')

# View for user registration
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('passwordr')
        email = request.POST.get('email')
        about = request.POST.get('about')
        talks_about = request.POST.get('talks_about')

        try:
            avatar = request.FILES['f-upload']
        except MultiValueDictKeyError:
            avatar = None

        if password == password_confirm:
            user = User.objects.create_user(
                username=username, password=password
            )
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            profile = Userprofile(
                person=user,
                about=about,
                talks_about=talks_about,
                avatar=avatar
            )
            profile.save()

            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error': True})
    return render(request, 'signup.html')

# View for displaying user profile
def user_profile(request, username, id):
    user = get_object_or_404(User, username=username, id=id)
    posts = Post.objects.filter(author=user)
    profile = get_object_or_404(Userprofile, person=user)
    return render(request, 'profile.html', {
        'profile': profile,
        'posts': posts,
    })

# View for updating user profile
@login_required(login_url='login')
def update_profile(request, username, id):
    user = get_object_or_404(User, username=username, id=id)
    profile = get_object_or_404(Userprofile, person=user)
    if request.method == 'POST':
        form = UserPForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username, id=user.id)
    else:
        form = UserPForm(instance=profile)
    return render(request, 'update_profile.html', {
        'form': form,
        'profile': profile,
    })

