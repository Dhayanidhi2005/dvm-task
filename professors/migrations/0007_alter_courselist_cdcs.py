# Generated by Django 5.0.3 on 2024-03-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0006_alter_evals_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courselist",
            name="cdcs",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FY", "First Year"),
                    ("SY1", "Second Year Sem 1"),
                    ("SY2", "Second Year Sem 1"),
                    ("TY1", "Third Year Sem 1"),
                    ("TY2", "Third Year Sem 2"),
                    ("4Y1", "Fourth Year Sem 1"),
                    ("4Y2", "Fourth Year Sem 2"),
                ],
                max_length=3,
            ),
        ),
    ]
