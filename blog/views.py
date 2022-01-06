from django.shortcuts import render, redirect
from django.views.generic import View

def index(request):
    print(request.user)
    return render(request, "blog/index.html")

class KakaoSignInView(View):
    def get(self, request):
        client_id = '아이디'
        redirect_uri = "https://blog-project-dhecm.run.goorm.io"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )

        
# class KakaoSignInCallbackView(View):
#     def get(self, request):

#         try:
#             code = request.GET.get("code")
#             client_id = 'f9776ceea93eb2574c9bbcfa49156cfb'
#             redirect_uri = "https://blog-project-dhecm.run.goorm.io"

#             token_request = requests.get(
#                 f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
#             )

#             token_json = token_request.json()
            
#             error = token_json.get("error",None)

#             if error is not None :
#                 return JsonResponse({"message": "INVALID_CODE"}, status = 400)

#             access_token = token_json.get("access_token")

#             #------get kakaotalk profile info------#

#             profile_request = requests.get(
#                 "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
#             )
#             profile_json = profile_request.json()

#             kakao_account = profile_json.get("kakao_account")
#             email = kakao_account.get("email", None)
#             kakao_id = profile_json.get("id")

#         except KeyError:
#             return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

#         except access_token.DoesNotExist:
#             return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
           
#         if Account.objects.filter(kakao_id = kakao_id).exists():
#             user = Account.objects.get(kakao_id = kakao_id)
#             token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
#             token = token.decode("utf-8")

#             return JsonResponse({"token" : token}, status=200)

#         else :
#             Account(
#                 kakao_id = kakao_id,
#                 email    = email,
#             ).save()

#             token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
#             token = token.decode("utf-8")

#             return JsonResponse({"token" : token}, status = 200)