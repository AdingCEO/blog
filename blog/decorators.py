from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse


# 관리자 권한 확인
def user_certification(function):
    def wrap(request, *args, **kwargs):
        print(request.user)
        print(post.user)
        if request.user.id == post.user.id:
            return function(request, *args, **kwargs)
        messages.info(request, "접근 권한이 없습니다.")
        return redirect('post-list')
    return wrap


# # 비로그인 확인
# def user_author(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.user != post.user:
#         return redirect('post-detail', post_id=post.id)