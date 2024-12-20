# Generated by Django 5.1.2 on 2024-11-07 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lws", "0008_subscribe"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="price",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="цена"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="price",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="цена"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="владелец",
            ),
        ),
    ]
