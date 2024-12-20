# Generated by Django 5.1.2 on 2024-10-25 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lws", "0003_alter_course_lessons"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="lessons",
        ),
        migrations.AddField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="courses",
                to="lws.course",
                verbose_name="уроки",
            ),
        ),
    ]
