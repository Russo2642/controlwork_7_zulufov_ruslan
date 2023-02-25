from django.shortcuts import render
from django.views import View

from book.models import Book


class IndexView(View):
    def get(self, request):
        books = Book.objects.exclude(status="BLOCKED")
        context = {
            'books': books
        }
        return render(request, 'index.html', context=context)
