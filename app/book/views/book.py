from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from book.models import Book

from book.forms import BookForm


class AddView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book_add.html', context={'form': form})

    def post(self, request):
        form = BookForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'book_add.html', context={'form': form})
        else:
            Book.objects.create(**form.cleaned_data)
            return redirect('index')
