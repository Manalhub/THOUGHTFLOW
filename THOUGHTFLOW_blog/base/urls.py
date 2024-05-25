from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('read_post/<str:id>/<str:slug>/', views.read_post, name='read_post'),
]