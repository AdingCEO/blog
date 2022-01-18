from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import CustomPasswordChangeView

# 미디어파일 처리 위한 import
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
    #all auth
    path(
        'email-confirmation-done/',
         TemplateView.as_view(template_name="blog/email_confirmation_done.html"),
         name='account_email_confirmation_done'
    ), # Template view 사용하면 view에 따로 작성 안해줘도 됨
    
    path(
        'password/change/',
        CustomPasswordChangeView.as_view(),
        name="account_password_change"
    ), #'allauth.urls'보다 위에 있어야 매칭 먼저됨
    
    path('', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)