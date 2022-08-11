from django.shortcuts import render
from .models import Post
from django.utils import timezone

# 요청(request)을 넘겨받아 render메서드를 호출합니다. 
# 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줍니다.

# 글목록을 published date 기준으로 정렬하기 위함.
# render함수에는 매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿이 있다.
# 튜플{} 에는 템플릿을 사용하기 위해 매개변수를 추가. 튜플{} 안에 있는 :이전에 문자열이 와야하고, 작은 따옴표''를 양쪽에 붙여야 함.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})