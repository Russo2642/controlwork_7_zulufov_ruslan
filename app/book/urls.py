from django.urls import path
from book.views.base import IndexView

from book.views.book import AddView, UpdateView, DeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', IndexView.as_view(), name='books'),
    path('books/add/', AddView.as_view(), name='book_add'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/confirm_delete/', DeleteView.as_view(), name='confirm_delete'),
]
