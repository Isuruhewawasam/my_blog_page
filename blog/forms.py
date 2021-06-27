from django import forms
from .models import Post, catgory

choices = catgory.objects.all().values_list('name', 'name')
choices_list = []
for items in choices:
    choices_list.append(items)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body','category','header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'auto_user_id', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
