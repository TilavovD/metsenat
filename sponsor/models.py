from django.db import models
from helpers.models import BaseModel

STATUS_TYPES = (
    ('new', 'Yangi'),
    ('moderation', 'Moderatsiyada'),
    ('confirmed', 'Tasdiqlangan'),
    ('cancel', 'Bekor qilingan'),
)

SPONSOR_TYPE = (
    ('physical', 'Jismoniy shaxs'),
    ('entity', 'Yuridik shaxs'),
)


class Sponsor(BaseModel):
    name = models.CharField("F.I.SH.", max_length=128)
    slug = models.CharField(max_length=128, unique=True, blank=True, null=True)
    phone_number = models.CharField("Telefon raqamingiz: +998", max_length=9)

    total_amount = models.DecimalField('Homiylik summasi', max_digits=12, decimal_places=2, default=0)
    spent_amount = models.DecimalField("Sarflangan summa", max_digits=12, decimal_places=2, default=0)

    status = models.CharField("Status", max_length=128, choices=STATUS_TYPES, default=STATUS_TYPES[3][0])
    sponsor_type = models.CharField("Qaysi turdagi shaxs", max_length=128, choices=SPONSOR_TYPE,
                                    default=SPONSOR_TYPE[0][0])

    company = models.CharField("Tashkilot", max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name
