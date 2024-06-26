# Generated by Django 5.0.3 on 2024-03-20 19:47

import django.db.models.deletion
import professors.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0002_alter_courselist_branch"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="branch",
            options={"verbose_name_plural": "Branches"},
        ),
        migrations.AlterModelOptions(
            name="courselist",
            options={"verbose_name_plural": "Course List"},
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
            options={
                "verbose_name_plural": "Announcements",
            },
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
                    "attachments",
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
    ]
