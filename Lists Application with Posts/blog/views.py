from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_list_author(request):
    posts = Post.objects.order_by('author')
    
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_list_published(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    
    return render(request, 'blog/post_list.html', {'posts':posts})        

def post_new(request):

  if request.method == "POST":
    form = PostForm(request.POST)

    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('blog:post_list')

  else:
    form = PostForm()

  return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
  
  post = get_object_or_404(Post, pk=pk)
  nickel = 3
  if request.method == "POST":
      form = PostForm(request.POST, instance=post)
      if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('blog:post_list')
  else:
      form = PostForm(instance=post)

  return render(request, 'blog/post_edit.html', {'form': form,'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.delete()
    
    return redirect('blog:post_list')


