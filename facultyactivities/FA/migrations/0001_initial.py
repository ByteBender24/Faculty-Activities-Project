# Generated by Django 5.0.3 on 2024-04-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminLogin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FacultyLogin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SDP_attended",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("staff_attended", models.CharField(max_length=100)),
                ("nature_of_event", models.CharField(max_length=100)),
                ("type_of_event", models.CharField(max_length=100)),
                ("name_of_event", models.CharField(max_length=100)),
                ("conducted_by", models.CharField(max_length=100)),
                ("no_of_days", models.IntegerField()),
                ("duration", models.CharField(max_length=100)),
                (
                    "proof_document",
                    models.FileField(max_length=250, upload_to="proof/"),
                ),
                ("academic_year", models.CharField(max_length=100)),
            ],
        ),
    ]
