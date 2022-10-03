from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from helpers.pagination import CustomPagination
from .models import Sponsor
from .serializer import SponsorCreateSerializer, SponsorListSerializer, SponsorDetailSerializer

from rest_framework.permissions import IsAuthenticated


class SponsorFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(label="F.I.SH", lookup_expr="contains")
    from_date = django_filters.DateFilter(label="Ushbu sanadan keyin", field_name='created_at', lookup_expr='gte')
    to_date = django_filters.DateFilter(label="Ushbu sanadan oldin", field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Sponsor
        fields = ('name', 'status', 'sponsor_type', 'total_amount', 'from_date', 'to_date')


class SponsorCreateView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SponsorFilterSet


class SponsorDetailView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset


class SponsorDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset
