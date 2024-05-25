from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate



# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render (request, 'login.html', {
                'error': True
                })
    return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('home')