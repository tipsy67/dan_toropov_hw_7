# Generated by Django 5.1.2 on 2024-11-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_user_last_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
