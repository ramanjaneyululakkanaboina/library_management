from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookListCreateView, BookDetailView, StudentBookListView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('student/books/', StudentBookListView.as_view(), name='student-book-list'),
]
