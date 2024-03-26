# Generated by Django 5.0.3 on 2024-03-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0010_alter_courses_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="Semester",
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
                    "sem",
                    models.CharField(
                        choices=[("S1", "Semester 1"), ("S2", "Semester 2")],
                        max_length=3,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("reg_date", models.DateField()),
                ("reg_date_last", models.DateField()),
            ],
        ),
    ]