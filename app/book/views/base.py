from django.shortcuts import render
from django.views import View

from book.models import Book


class IndexView(View):
    def get(self, request):
        search_name = request.GET.get('search')
        if search_name:
            books = Book.objects.filter(name__icontains=search_name).exclude(status="BLOCKED")
        else:
            books = Book.objects.exclude(status="BLOCKED")
        context = {
            'books': books
        }
        return render(request, 'index.html', context=context)
