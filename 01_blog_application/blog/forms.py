from .models import Comment
from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your email',
            'required': 'required'
        })
    )
    to = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Recipient email',
            'required': 'required'
        })
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Your comments (optional)',
            'rows': 5
        })
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'body': forms.Textarea(attrs={'class': 'form-textarea'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
