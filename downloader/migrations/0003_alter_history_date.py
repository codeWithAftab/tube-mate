# Generated by Django 4.0.4 on 2022-07-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0002_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
