from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'email', 'text')
        labels = {
            'name': 'Имя автора',
            'email': 'Почта автора',
            'text': 'Текст автора'
        }


class SearchForm(forms.Form):
    query = forms.CharField()
