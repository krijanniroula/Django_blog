from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from blog.models import BlogPost

# Create your views here.

def add_comment_to_blog(request,slug):
    post = get_object_or_404(BlogPost,slug=slug)
    form = CommentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form = CommentForm()
    template_name = 'comments/view.html'
    context = {'form': form,'post':post}
    return render(request, template_name, context)
