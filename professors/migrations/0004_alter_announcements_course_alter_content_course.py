# Generated by Django 5.0.3 on 2024-03-20 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professors", "0003_alter_branch_options_alter_courselist_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcements",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="professors.courselist"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="professors.courselist"
            ),
        ),
    ]
