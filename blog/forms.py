from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField()
  receiver = forms.EmailField()
  comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':10, 'cols':30}))
 
class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ('name', 'email', 'body')
      widgets={
        'body': forms.Textarea(attrs={'rows':10, 'cols':30})
        }