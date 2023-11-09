from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

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