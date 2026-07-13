from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

