# Generated by Django 5.0.3 on 2024-03-17 12:59

import django.db.models.deletion
import professors.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("students", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("dept", models.CharField(max_length=50)),
                ("branchs", models.JSONField()),
                ("cdcs", models.JSONField()),
                ("dels", models.JSONField()),
                ("opels", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Courses",
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
                ("course_id", models.CharField(max_length=10)),
                ("course_name", models.CharField(max_length=20)),
                ("marks", models.IntegerField()),
                ("grade", models.CharField(max_length=2)),
                ("students", models.ManyToManyField(to="students.students")),
                (
                    "dept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professors.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Content",
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
                ("title", models.CharField(max_length=100)),
                (
                    "attachemnts",
                    models.FileField(
                        upload_to=professors.models.custom_path_for_content
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professors.courses",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professors",
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
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("HOD", "Head of Departemnt"),
                            ("PRO", "Professor"),
                            ("AIP", "Assistant Professor"),
                            ("AOP", "Associate Professor"),
                        ],
                        max_length=3,
                    ),
                ),
                ("courses", models.ManyToManyField(to="professors.courses")),
                (
                    "dept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professors.department",
                    ),
                ),
                (
                    "prof",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Announcements",
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
                ("title", models.CharField(max_length=100)),
                ("msg", models.TextField()),
                (
                    "attachments",
                    models.FileField(
                        upload_to=professors.models.custom_path_for_announcement
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="professors.courses",
                    ),
                ),
                (
                    "prof",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="professors.professors",
                    ),
                ),
            ],
        ),
    ]