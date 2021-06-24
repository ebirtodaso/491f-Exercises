from django import forms

from .models import Post

class PostForm(forms.ModelForm):

  class Meta:
      model = Post
      fields = ('title', 'text',)


class SortForm(forms.Form):
  SORT_OPTIONS = [(' ', ' '),
                  ('author', 'author'),
                  ('title', 'title'),
                  ('text', 'text'),
                  ]
  ORDER_OPTIONS = [(' ', ' '),
                  ('created_date', 'created_date'),
                  ('published_date', 'published_date'),
                  ]
                  
                  
  filter_by = forms.ChoiceField(choices=SORT_OPTIONS)
  filter_string = forms.CharField(max_length=200, required=False)
  #filter_string.label.Hide()
  order_by = forms.ChoiceField(choices=ORDER_OPTIONS)

