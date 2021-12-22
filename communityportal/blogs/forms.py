from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Posts 
        fields = ['title','description']
        labels = {'title':'Title','description':'Description'}
        widgets = {'title':forms.TextInput , 'description':forms.Textarea}        