# Generated by Django 5.1.2 on 2024-10-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lws', '0002_alter_course_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(blank=True, related_name='courses', to='lws.lesson', verbose_name='уроки'),
        ),
    ]
