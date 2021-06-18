from django.views import generic
from django.urls import reverse_lazy
from .models import listItem
from .forms import doneBox

class IndexView(generic.ListView):
    template_name = 'list/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        """Return the all items in list."""
        return listItem.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'list/create.html'
  model = listItem
  fields = ['item']
  success_url = reverse_lazy( 'lists:index')

class UpdateView(generic.edit.UpdateView):
    template_name =  'list/update.html'
    model = listItem
    fields = ['item']
    success_url = reverse_lazy( 'lists:index')

class DeleteView(generic.edit.DeleteView):
    template_name =  'list/delete.html' # override default of listItems listItem_confirm_delete.html
    model = listItem
    success_url = reverse_lazy( 'lists:index')