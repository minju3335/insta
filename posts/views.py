from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        # 두 번째 인자에 POST정보 넣기
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 현재 유저
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form':form,
    }

    return render(request, 'form.html', context)


@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    # 이미 좋아요 버튼을 누른 경우 (없애는 것)
    if post in user.like_posts.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
        # user.like_posts.add(post)

    return redirect('posts:index')