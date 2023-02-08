from django.db import models

class Car(models.Model):
    vin = models.CharField(verbose_name='vin', db_index=True, unique=True, max_length=70)
    color = models.CharField(verbose_name='color', max_length=70)
    brand = models.CharField(verbose_name='brand', max_length=70)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField()