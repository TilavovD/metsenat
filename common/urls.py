from django.urls import path
from .views import StudentSponsorCreateView, StudentSponsorListView, Dashboard, DashboardLineGraphStudent, \
    DashboardLineGraphSponsor

urlpatterns = [
    path("add", StudentSponsorCreateView.as_view(), name="student-sponsor-add"),
    path("list", StudentSponsorListView.as_view(), name="student-sponsor-list"),
]
