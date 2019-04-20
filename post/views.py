from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post, Comments
from post.forms import CommentForm


def posts_list(request):
    post = Post.objects.all()
    return render(request, 'post/post_list.html', {'post': post})


def post_card(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = Comments.objects.filter(post=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect(post_card, pk)
    else:
        form = CommentForm()
    return render(request, 'post/post_card.html',
                  {'post': post,
                   # 'comments': comment,
                   'form': form})
