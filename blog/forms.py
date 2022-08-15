from django import forms
from .models import Post

# 뷰에서 이 폼을 사용 템플릿에서 보여주게 해줘야 한다.
# 링크, URL, 뷰 그리고 템플릿을 만들어야 한다.
# Form의 이름이 PostForm 이라고 선언하고 그 양식은 ModelForm 이라고 지정한다.
class PostForm (forms.ModelForm):
    # Form에 사용되는 모델이 Post 임을 선언한다.
    class Meta:
        model = Post
        fields = ('title','text')