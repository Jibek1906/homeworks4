from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14)
    age = models.PositiveIntegerField(default=18)
    experience = models.FloatField(default=0, null=True)
    gender = models.CharField(max_length=1,choices=GENDER)
    salary = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.salary = 'Для работы в нашей компании вам не хватает опыта'
        elif 1 <= self.experience < 3:
            self.salary = '1000$'
        elif 3 <= self.experience < 7:
            self.salary = '2000$'
        elif 7 <= self.experience <= 10:
            self.salary = '5000$'
        else:
            self.salary = 'Для обсуждения зарплаты подойдите к нам офис'
        
        super().save(*args, **kwargs)