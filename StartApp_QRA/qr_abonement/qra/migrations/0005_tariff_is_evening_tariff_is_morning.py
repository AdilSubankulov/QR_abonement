# Generated by Django 5.1.2 on 2024-10-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qra', '0004_remove_tariff_duration_days_tariff_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='is_evening',
            field=models.BooleanField(default=False, verbose_name='16:00 до 23:00'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='is_morning',
            field=models.BooleanField(default=False, verbose_name='08:00 до 16:00'),
        ),
    ]
