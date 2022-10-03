import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated
from helpers.pagination import CustomPagination
from .models import Student, University
from .serializer import StudentCreateSerializer, StudentListSerializer, StudentDetailSerializer, \
    CreateUniversitySerializer


class StudentFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(label="F.I.SH", lookup_expr="contains")

    class Meta:
        model = Student
        fields = ('name', 'degree', 'university')


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    permission_classes = [IsAuthenticated]


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilterSet


class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset


class StudentDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])

        return queryset


class CreateUniversityView(CreateAPIView):
    queryset = University.objects.all()
    serializer_class = CreateUniversitySerializer
    permission_classes = [IsAuthenticated]
