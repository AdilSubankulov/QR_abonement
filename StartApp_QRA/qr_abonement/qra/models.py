from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from datetime import date

from rest_framework import request


class Tariff(models.Model):
    DURATION_TYPE_CHOICES = [
        ('days', 'Fixed Number of Days'),  # фиксированное количество дней
        ('period', 'Period Duration'),     # интервал времени
    ]

    name = models.CharField(max_length=100, verbose_name="Tariff Name")
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Price")
    duration_type = models.CharField(max_length=10, choices=DURATION_TYPE_CHOICES, default='days', verbose_name="Duration Type")
    start_date = models.DateField(null=True, blank=True, verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    max_visits = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)], verbose_name="Maximum Visits")
    is_morning = models.BooleanField("08:00-16:00", default=False)
    is_evening = models.BooleanField("16:00-23:00", default=False)
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    def clean(self):
        from django.core.exceptions import ValidationError
        # Проверка, что start_date и end_date заполнены только для типа 'period'
        if self.duration_type == 'period':
            if not self.start_date or not self.end_date:
                raise ValidationError(_("Start Date and End Date must be set for period-based tariffs."))
            if self.start_date >= self.end_date:
                raise ValidationError(_("End Date must be after Start Date."))
        elif self.duration_type == 'days':
            # Очищаем даты, если тип - дни, чтобы избежать путаницы
            self.start_date = None
            self.end_date = None

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    unique_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

class UserAbonement(models.Model):
    unique_id = models.AutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE)
    days_count = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_profile.full_name} - {self.tariff.name}"
