from django import forms
from .models import Post, Comment, User, Profile

#validator 위한 import
# from .validators import validate_symbols
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    # model에 없는 컬럼도 form에서 써서 만들 수 있음. 적용은 어떻게 할 수 있을지 모르겠넴
    # memo = forms.CharField(max_length=80, validators=[validate_symbols])
    class Meta:
        model = Post
        fields = ['title','content','place', 'member', 'image1', 'image2', 'image3', 'user'] # '__all__'
        widgets = {
            "member":forms.RadioSelect,
        }
        
    #model딴의 유효성 검사보다 form딴의 유효성 검사가 먼저 일어남
    def clean_title(self): # clean_field를 사용해서 Form에서 유효성검사하기
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
        return title
    

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= '__all__'

        
class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=50)
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'
        widgets={
            'intro':forms.Textarea,
        }
        
        
#회원가입 form 수정하기. settings에 이 폼 쓴다고 말해줘야함
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "nickname"]
        
    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.nickname = self.cleaned_data["nickname"]
        user.save()
        
        
        