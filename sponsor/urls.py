from django.urls import path
from .views import SponsorCreateView, SponsorListView, SponsorDetailView, SponsorDetailUpdateView

urlpatterns = [
    path('register', SponsorCreateView.as_view(), name='sponsor-register'),
    path('list', SponsorListView.as_view(), name='sponsor-list'),
    path('<str:slug>', SponsorDetailView.as_view(), name='sponsor-detail'),
    path('update/<str:slug>', SponsorDetailUpdateView.as_view(), name='sponsor-update'),
]
