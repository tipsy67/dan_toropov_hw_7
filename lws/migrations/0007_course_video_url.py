# Generated by Django 5.1.2 on 2024-11-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lws", "0006_alter_course_options_course_owner_lesson_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="video_url",
            field=models.URLField(blank=True, null=True, verbose_name="ссылка"),
        ),
    ]
