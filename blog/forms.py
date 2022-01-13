from django import forms
from .models import Post

#validator 위한 import
# from .validators import validate_symbols
from django.core.exceptions import ValidationError

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=50, label='제목')
#     content = forms.CharField(label='내용', widget=forms.Textarea)
#     place = forms.CharField(max_length=50, label='장소')
#     member = forms.IntegerField(label='모인 사람 수', help_text='숫자로 써주세요. ex)2')
#     image = forms.ImageField(required=False)


class PostForm(forms.ModelForm):
    # model에 없는 컬럼도 form에서 써서 만들 수 있음. 적용은 어떻게 할 수 있을지 모르겠넴
    # memo = forms.CharField(max_length=80, validators=[validate_symbols])
    
    class Meta:
        model = Post
        fields = ['title','content','place', 'member', 'image', 'user'] # '__all__'
    
    #model딴의 유효성 검사보다 form딴의 유효성 검사가 먼저 일어남
    def clean_title(self): # clean_field를 사용해서 Form에서 유효성검사하기
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함될 수 없습니다.')
        return title