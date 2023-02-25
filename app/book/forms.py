from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя автора')
    email = forms.EmailField(max_length=300, required=True, label='Почта автора')
    text = forms.CharField(max_length=3000, required=True, label='Текст автора', widget=widgets.Textarea)
