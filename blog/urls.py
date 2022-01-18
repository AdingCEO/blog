from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/new/', views.post_create, name='post-create'),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/<int:post_id>/edit/', login_required(views.post_update), name='post-update'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post-delete'),
    
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('profile/<int:user_id>/posts/', views.user_posts, name='user_posts'),
    path('set-profile/', login_required(views.set_profile), name='set_profile'),
    path('update-profile/', login_required(views.update_profile), name='update_profile'),

    path('posts/comment/delete/<int:post_id>/<int:comment_id>/', views.comment_delete, name='comment_delete')
]
