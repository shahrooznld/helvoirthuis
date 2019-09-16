from django import forms
from .models import Contact


class Registrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        }))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))

    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')],
                                 widget=forms.Select(
                                     attrs={
                                        'class': 'form-control'
                                     }
                                 ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Subject'
        }
    ),
        required=False)
    body = forms.CharField(label='Comment', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write your text...'}))

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'category',
            'subject',
            'body'
        )
