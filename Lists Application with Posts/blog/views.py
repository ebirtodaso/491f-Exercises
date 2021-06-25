from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import PostForm, SortForm
from .models import Post

class PostView(generic.ListView):
  model = Post
  form_class = SortForm
  template_name = "blog/post_list.html"
  context_object_name = 'posts'

  def get_queryset(self):
    context = Post.objects.all()

    choice = self.request.GET.get('choice', None)
    filter_text = self.request.GET.get('filter', None)
    order = self.request.GET.get('order', None)

    if (filter_text and choice) is not None:
      if choice == '1':
        context = Post.objects.filter(text__contains=filter_text)

    if order is not None:
      if order == '1':
        context = context.order_by('published_date')
      if order == '2':
        context = context.order_by('-published_date')

    return context

#Creates a new post
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


