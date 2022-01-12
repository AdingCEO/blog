from django.shortcuts import render, redirect
from django.views.generic import View

class KakaoSignInView(View):
    def get(self, request):
        client_id = '아이디'
        redirect_uri = "http://blog-project-dhecm.run.goorm.io/kakao/login/callback/"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

def index(request):
    print(request.user)
    return render(request, "blog/index.html")

