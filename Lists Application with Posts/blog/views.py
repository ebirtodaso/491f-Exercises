from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import PostForm, SortForm
from .models import Post

class UpdateView(generic.edit.FormMixin, generic.ListView):
  
  def get(self, request, *args, **kwargs):
      # From ProcessFormMixin
      form_class = self.get_form_class()
      self.form = self.get_form(form_class)

      # From BaseListView
      self.object_list = self.get_queryset()
      allow_empty = self.get_allow_empty()
      if not allow_empty and len(self.object_list) == 0:
          raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                        % {'class_name': self.__class__.__name__})

      context = self.get_context_data(object_list=self.object_list, form=self.form)
      return self.render_to_response(context)

  def post(self, request, *args, **kwargs):
      return self.get(request, *args, **kwargs)



class PostView(UpdateView):
  model = Post
  form_class = SortForm
  template_name = "blog/post_list.html"
  context_object_name = 'posts'
  #filter_string = self.form['filter_string']

  def get_queryset(self):
    #data = 
    #self.request.
    #order = 'created_date'
    #new_context = Post.objects.filter(
                                      #text=filter_val,
                                      #).order_by(order)

    #return new_context

  #def get_context_data(self, **kwargs):
    #context = super(PostView, self).get_context_data(**kwargs)
    #context['string'] = self.request.GET.get('filter', 'Test')
    #context['orderby'] = self.request.GET.get('orderby', 'created_date')
    #return context

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


