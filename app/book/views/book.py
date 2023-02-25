from django.contrib.postgres.search import SearchVector
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


class UpdateView(View):
    def get(self, request, pk):
        books = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=books)
        return render(request, 'book_update.html',
                      context={
                          'form': form,
                          'books': books
                      })

    def post(self, request, pk):
        books = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'book_update.html', context={'form': form})


class DeleteView(View):
    def get(self, request, pk):
        books = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=books)
        return render(request, 'book_confirm_delete.html',
                      context={
                          'books': books,
                          'form': form
                      })

    def post(self, request, pk):
        books = get_object_or_404(Book, pk=pk)
        books.delete()
        return redirect('index')
