from django.urls import path
from .views import StudentCreateView, StudentListView, StudentDetailView, StudentDetailUpdateView

urlpatterns = [
    path('register', StudentCreateView.as_view(), name='student-register'),
    path('list', StudentListView.as_view(), name='student-list'),
    path('<str:slug>', StudentDetailView.as_view(), name='student-detail'),
    path('update/<str:slug>', StudentDetailUpdateView.as_view(), name='student-update'),
]
