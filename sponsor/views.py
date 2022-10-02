from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Sponsor
from .serializer import SponsorCreateSerializer, SponsorListSerializer, SponsorDetailSerializer


class SponsorCreateView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer


class SponsorDetailView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset


class SponsorDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset

