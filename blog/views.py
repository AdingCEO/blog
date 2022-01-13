from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

class KakaoSignInView(View):
    def get(self, request):
        client_id = '아이디'
        redirect_uri = "http://blog-project-dhecm.run.goorm.io/kakao/login/callback/"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )


def post_list(request):
    posts = Post.objects.order_by('-dt_created')
    paginator = Paginator(posts, 8) # post 8개를 1 page로 가지는 paginator 객체
    curr_page_number = request.GET.get('page') #GET요청의 쿼리스트링의 page 파라미터의 값을 얻어옴
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number) # 쿼리스트링에서 가져온 현재 페이지를 알려주는 애
    return render(request, 'blog/post_list.html', {'page':page}) # 현재 페이지의 페이지 객체를 context로 넘겨줌


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)





#post_create를 form.Form으로 구현

# def post_create(request):
#     # POST요청이면 바인딩
#     if request.method=='POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         place = request.POST['place']
#         member = request.POST['member']
#         image = request.POST['image']
#         new_post = Post(
#             user=request.user,
#             title=title,
#             content = content,
#             place = place,
#             member = member,
#             image = image,
#         )
#         post_form = PostForm(new_post)
#         #여기부터 안됨.. is_valid함수가 안먹음 ㅠ
#         if post_form.is_valid():
#             # 통과하면 db에 저장됨
#             post_form.save()
#             return redirect('post-detail', post_id=post_form.id)
#         else:
#             # 유효하지 않으면 발생한 에러 메세지와 함께 작성한 폼 전달됨
#              return render(request, 'blog/post_form.html', {'form':post_form})
#     else:
#         post_form = PostForm()
#         return render(request, 'blog/post_form.html', {'form':post_form})


#post_create를 form.ModelForm으로 구현

def post_create(request):
    # POST요청이면 바인딩
    if request.method=='POST':
        post_form = PostForm(request.POST) # 만들어 놓은 폼인 PostForm과 post요청으로 들어온 data를 바인딩
        if post_form.is_valid(): # 유효성 검증
            new_post = post_form.save() # 통과하면 db에 저장됨
            return redirect('post-detail', post_id=new_post.id)
        else:
            # 유효하지 않으면 발생한 에러 메세지와 함께 바인딩된 폼 인스턴스가 전달됨
             return render(request, 'blog/post_form.html', {'form':post_form})
    else:
        post_form = PostForm()
        return render(request, 'blog/post_form.html', {'form':post_form})
    
    
    
    
    
    
def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method=='POST':
        post_form = PostForm(request.POST, instance=post) #새로운 form instance를 사용한다는게 아니라 기존에 작성된 Post모델 instance를 사용한다는 뜻
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form':post_form})
    
    
def post_delete(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete() # 템플릿에 현재 주소로 post요청 보내는 버튼 만들어두고 post요청이 들어오면 삭제됨
        return redirect('post-list')
    else:
        return render(request, 'blog/post_confirm_delete.html', {'post':post})