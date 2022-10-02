from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializer import StudentCreateSerializer, StudentListSerializer, StudentDetailSerializer


class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset


class StudentDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('slug', None):
            queryset = queryset.filter(slug=self.kwargs['slug'])
        return queryset
