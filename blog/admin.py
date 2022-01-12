from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from blog.models import User, Profile, Post, Comment, Tag

# adminmodel 등록방법
# 1. admin.site.register(User, UserAdmin)

# 2. class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'created_at', 'updated_at' ]
# admin.site.register(Post, PostAdmin)

#3. 장식자 형태로 등록
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email'
    ]
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass   

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass   

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass