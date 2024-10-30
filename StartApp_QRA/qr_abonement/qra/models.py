from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from datetime import date

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

# class Provider(models.Model):
#     pass
#
# class UserProfile(models.Model):
#     pass
#
# class UserSubscription(models.Model):
#     pass
#
# class Visit(models.Model):
#     pass
