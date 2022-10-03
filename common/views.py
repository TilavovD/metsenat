import django_filters
from django.db.models import Sum, Count
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from sponsor.models import Sponsor
from .models import StudentSponsor
from student.models import Student

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializer import StudentSponsorSerializer, StudentSponsorListSerializer
from helpers.pagination import CustomPagination


class StudentSponsorFilterSet(django_filters.FilterSet):
    student_name = django_filters.CharFilter(label="Talabaning ismi", lookup_expr="contains",
                                             field_name='student__name')
    sponsor_name = django_filters.CharFilter(label="Homiyning ismi", lookup_expr="contains", field_name='sponsor__name')

    class Meta:
        model = StudentSponsor
        fields = ('student_name', 'sponsor_name')


class StudentSponsorCreateView(CreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer


class StudentSponsorListView(ListAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorListSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentSponsorFilterSet


class Dashboard(APIView):
    def get(self, request):
        data = Student.objects.aggregate(total_received=Sum('received_amount'), total_contract=Sum("total_contract"))
        print(data["total_contract"])
        return Response({"Jami so'ralgan summa": f"{data['total_contract']} UZS",
                         "Jami to'langan summa": f'{data["total_received"]} UZS',
                         "To'lanishi kerak bo'lgan summa": f'{data["total_contract"] - data["total_received"]} UZS'})


class DashboardLineGraphStudent(APIView):
    def get(self, request):
        queryset = (Student.objects.values('created_at').annotate(count=Count('created_at')).order_by())

        return Response(queryset)


class DashboardLineGraphSponsor(APIView):
    def get(self, request):
        queryset = (Sponsor.objects.values('created_at').annotate(count=Count('created_at')).order_by())

        return Response(queryset)
