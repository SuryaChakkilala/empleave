# Generated by Django 4.1.6 on 2023-04-21 10:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pages", "0002_vacationslot_uservacationdetails"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserVacationDetails", new_name="UserVacation",
        ),
    ]
