from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from helpers.models import BaseModel
from student.models import Student
from sponsor.models import Sponsor


# Create your models here.

class User(AbstractUser):
    INVALID_CODE = "######"

    full_name = models.CharField(_("full name"), max_length=256)

    created_at = models.DateTimeField(_("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("date updated"), auto_now=True)

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")


class StudentSponsor(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sponsor")
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="student")
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.student.name} received {self.amount} UZS from {self.sponsor.name}"
