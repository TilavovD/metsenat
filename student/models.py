from django.db import models
from helpers.models import BaseModel

from django.db.models.signals import post_save
from django.dispatch import receiver


class University(BaseModel):
    name = models.CharField("Nomi", max_length=128)

    def __str__(self):
        return self.name


DEGREE = (
    ('bachelor', 'Bakalavr'),
    ('master', 'Magistr'),
)


class Student(BaseModel):
    name = models.CharField("F.I.SH", max_length=128)
    slug = models.CharField(max_length=128, unique=True, blank=True, null=True)
    phone_number = models.CharField("Telefon raqam: +998", max_length=9)

    degree = models.CharField('Talabalik turi', max_length=128, choices=DEGREE, default=DEGREE[0][0])
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='student')

    total_contract = models.DecimalField("Kontrakt miqdori", max_digits=12, decimal_places=2, default=0)
    received_amount = models.DecimalField("Ajratilgan summa", max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "student"
        verbose_name_plural = 'students'


# @receiver(post_save, sender=Student)
# def my_handler(sender, **kwargs):
#     print(1)
