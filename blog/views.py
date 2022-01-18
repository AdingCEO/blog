from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View
from django.db.models import Q
from .models import Post, User, Comment
from .forms import PostForm, CommentForm, ProfileForm, SearchForm
from django.core.paginator import Paginator

#decorator 관련 import
from .decorators import *
from django.contrib.auth.decorators import login_required, user_passes_test

#비밀번호 변경시에 리디렉션 만들어주기위해서 임포트
from allauth.account.views import PasswordChangeView


#로그인 관련
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self): # overriding
        return reverse('post-list')
    

class KakaoSignInView(View):
    def get(self, request):
        client_id = '아이디'
        redirect_uri = "http://blog-project-dhecm.run.goorm.io/kakao/login/callback/"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

    
#post관련
def post_list(request):
    context={}
    search_form = SearchForm()
    context['form']=search_form
    
    if request.method=='POST':
        searchWord = request.POST['search_word']
        posts = Post.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord) | Q(place__icontains=searchWord)).distinct().order_by('-dt_created')
    else:
        posts = Post.objects.order_by('-dt_created')

    paginator = Paginator(posts, 8) # post 8개를 1 page로 가지는 paginator 객체
    curr_page_number = request.GET.get('page') #GET요청의 쿼리스트링의 page 파라미터의 값을 얻어옴
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number) # 쿼리스트링에서 가져온 현재 페이지를 알려주는 애
    context['page']=page
    return render(request, 'blog/post_list.html', context) # 현재 페이지의 페이지 객체를 context로 넘겨줌


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()
    # 댓글 작성을 위한 로직 구현
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        new_comment = comment_form.save()
        return redirect('post-detail', post_id=new_comment.post.id) # 안되면 post.id해보기
    else:
        comment_form = CommentForm()
        context = {'form':comment_form, 'post':post, 'comments':comments}
        return render(request, 'blog/post_detail.html', context)


@login_required
def post_create(request):
    # POST요청이면 바인딩
    if request.method=='POST':
        post_form = PostForm(request.POST, request.FILES) # 만들어 놓은 폼인 PostForm과 post요청으로 들어온 data를 바인딩
        if post_form.is_valid(): # 유효성 검증
            new_post = post_form.save() # 통과하면 db에 저장됨
            return redirect('post-detail', post_id=new_post.id)
        else:
            # 유효하지 않으면 발생한 에러 메세지와 함께 바인딩된 폼 인스턴스가 전달됨
             return render(request, 'blog/post_form.html', {'form':post_form})
    else:
        post_form = PostForm()
        return render(request, 'blog/post_form.html', {'form':post_form})
    
    
# @login_required 얘는 urls.py에서 해줌
def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method=='POST':
        post_form = PostForm(request.POST, request.FILES, instance=post) #새로운 form instance를 사용한다는게 아니라 기존에 작성된 Post모델 instance를 사용한다는 뜻
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form':post_form})

    
# class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     form_class = PostForm
#     tempalte_name = 'blog/post_form.html'
#     pk_url_kwarg='post_id'
#     raise_exception = True # 404
#     redirect_unauthenticated_users = False #True면 로그인 안된애는 로그인페이지로감 로그인 된애는 raise_exception에 따라서 됨
    
#     def get_success_url(self):
#         return reverse('post-detail', kwargs={'review_id':sekf.object.id})
    
#     def test_func(self, user): # UserPassesTestMixin의 테스트함수. True이면 뷰에 접근가능
#         post = self.get_object()
#         return post.user == user
    

@login_required
def post_delete(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.user.id==post.user.id:
        if request.method == 'POST':
            post.delete() # 템플릿에 현재 주소로 post요청 보내는 버튼 만들어두고 post요청이 들어오면 삭제됨
            return redirect('post-list')
        else:
            return render(request, 'blog/post_confirm_delete.html', {'post':post})
    else:
        return redirect('post-detail', post_id=post_id)

    
# class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     form_class = PostForm
#     tempalte_name = 'blog/post_confirm_delete.html'
#     pk_url_kwarg='post_id'
#     raise_exception = True # 404
    
#     def get_success_url(self):
#         return reverse('post-list')
    
#     def test_func(self, user):
#         post = self.get_object()
#         return post.user == user    



# profile 관련

def user_profile(request, user_id):
    user=User.objects.get(id=request.user.id)
    profile_user = User.objects.get(id=user_id)
    profile_user_posts = profile_user.post_set.all().order_by('-dt_created')[:4]
    context = {'user':user, 'profile_user':profile_user, 'profile_user_posts':profile_user_posts}
    return render(request, 'blog/profile.html', context)

    
def set_profile(request):
    if request.method=='POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid(): # 유효성 검증
            new_profile = profile_form.save() # 통과하면 db에 저장됨
            return redirect('post-list')
        else:
            # 유효하지 않으면 발생한 에러 메세지와 함께 바인딩된 폼 인스턴스가 전달됨
             return render(request, 'blog/post_form.html', {'form':profile_form})
    else:
        profile_form = ProfileForm()
        return render(request, 'blog/profile_form.html', {'form':profile_form})
    
    
def update_profile(request):
    user=User.objects.get(id=request.user.id)
    profile = user.profile
    if request.method=='POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile) #새로운 form instance를 사용한다는게 아니라 기존에 작성된 Post모델 instance를 사용한다는 뜻
        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile', user_id=user.id)
    else:
        profile_form = ProfileForm(instance=profile)
        return render(request, 'blog/profile_form.html', {'form':profile_form})
    
    
def user_posts(request, user_id):
    # user = User.objects.get(id=user_id)
    user = get_object_or_404(User, id=user_id)
    posts = user.post_set.all().order_by('-dt_created')
    paginator = Paginator(posts, 8)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'blog/profile_posts.html', {'user':user, 'page':page, 'paginator':paginator})



def comment_delete(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('post-detail', post_id)
    