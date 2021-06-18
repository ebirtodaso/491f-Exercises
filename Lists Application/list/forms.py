from django import forms
from .models import listItem

class doneBox(forms.Form):
  isDone = forms.BooleanField()

  class Meta:
    model = listItem
