# Generated by Django 4.1.1 on 2022-10-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_alter_sponsor_company_alter_sponsor_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
    ]
