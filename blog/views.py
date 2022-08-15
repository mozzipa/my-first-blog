from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# 요청(request)을 넘겨받아 render메서드를 호출합니다. 
# 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줍니다.

# 글목록을 published date 기준으로 정렬하기 위함.
# render함수에는 매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿이 있다.
# 튜플{} 에는 템플릿을 사용하기 위해 매개변수를 추가. 튜플{} 안에 있는 :이전에 문자열이 와야하고, 작은 따옴표''를 양쪽에 붙여야 함.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

# base.html에서 post_detail link를 활성화하면, urls.py를 통해서 해당 url을 확인한다.
# urls.py 는 views.py에 post_detail 함수가 있다고 선언해주고,
# views.py에서 post_detail을 위해 pk 값을 받고 post_detail.html을 연다.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

# urls.py에서 작성된 post_new 링크를 열었을 때, post_new.html을 열기위한 함수
def post_new(request):
    # 폼에 입력된 데이터를 view 페이지로 가지고 올 때, request로 넘겨받은 request.POST 데이터를 확인하고 양식에 채워넣기 위함.
    if request.method == "POST":
        form = PostForm(request.POST)
        # Post 모델에 저장하기 전에 작성자와 published_date를 추가함.
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # 작성하고 save 한 이후에 detail page로 넘어가도록 함.
            return redirect('post_detail',pk=post.pk)
    # request 가 비어있는 경우
    else :
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    # post_new와 달리 pk 값도 받아온다.
    # get_object_or_404(Post, pk=pk)를 호출하여 수정하고자 하는 글의 Post 모델 instance를 가져온다. (pk로 원하는 글을 찾는다.)
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 가져온 데이터를 폼에, 글을 만들 때 입력했던 데이터가 있게 한다.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # post_new와 달리 post를 가져온다.
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
