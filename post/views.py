from django.shortcuts import render, get_object_or_404
from post.models import Post


def posts_list(request):
    post = Post.objects.all()
    return render(request, 'post/post_list.html', {'post': post})

def post_card(request, pk):
  post = get_object_or_404(Post, id=pk)
  return render(request, 'post/post_card.html', {'post': post})
