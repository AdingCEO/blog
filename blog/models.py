from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=15, unique=True, null=True)
    
    def __str__(self):
        return self.email
    
    
    
class Profile(models.Model):
    user = models.OneToOneField('blog.User', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    army=models.CharField(max_length=50)
    
    def __str__(self):
        return self.user
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    place = models.CharField(max_length=50)
    member = models.IntegerField()
    image = models.ImageField(blank=True)
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    dt_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    tag_set = models.ManyToManyField('blog.Tag', blank=True)
    user = models.ForeignKey('blog.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE) # post_id 필드 생성됨
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    dt_modified = models.DateTimeField(auto_now=True, verbose_name="Date Modified")
    
    def __str__(self):
        return self.message
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name