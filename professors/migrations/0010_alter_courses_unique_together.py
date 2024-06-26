# Generated by Django 5.0.3 on 2024-03-22 13:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0009_alter_courses_unique_together"),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="courses",
            unique_together={("student", "course", "date_added")},
        ),
    ]
