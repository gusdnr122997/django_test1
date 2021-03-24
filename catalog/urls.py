from django.urls import path
from catalog import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path(r'authors/', views.AuthorListView.as_view(), name='authors'),
    path(r'author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path('allbooks/', views.LoanedBooksByAllUserListView.as_view(), name='all-borrowed'),
]

urlpatterns += [
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]