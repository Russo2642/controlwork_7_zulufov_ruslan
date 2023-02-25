from django.urls import path
from book.views.base import IndexView

from book.views.book import AddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', IndexView.as_view(), name='books'),
    path('books/add/', AddView.as_view(), name='book_add'),
]
