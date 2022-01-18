from django.db import models
from django.contrib.auth.models import AbstractUser

#유효성검사 import
from django.core.validators import MinLengthValidator #built-in validators
from .validators import validate_symbols

class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.email
    
    
    
class Profile(models.Model):
    user = models.OneToOneField('blog.User', on_delete=models.CASCADE)
    intro = models.CharField(blank=True, max_length=60)
    address = models.CharField(max_length=100)
    army=models.CharField(max_length=50)
    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.address
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={'unique':'이미 있는 제목입니다'})
    content = models.TextField(validators=[MinLengthValidator(2, '2글자 이상 적어줘잉'), validate_symbols])
    place = models.CharField(max_length=50)
    
    MEMBER_CHOICES = [
        (1, "혼자"),
        (2, "둘이"),
        (3, "셋이"),
        (4, "넷"),
        (5, "다섯"),
        (6, "여섯"),
        (7, "일곱"),
        (8, "여덟"),
    ]
    
    member = models.IntegerField(choices=MEMBER_CHOICES, default=None)
    
    image1 = models.ImageField(blank=True, upload_to='pics')
    image2 = models.ImageField(blank=True, upload_to='pics')
    image3 = models.ImageField(blank=True, upload_to='pics')
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    dt_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    user = models.ForeignKey('blog.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE) # post_id 필드 생성됨
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    dt_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    
    def __str__(self):
        return self.message