from django.db import models

# Create your models here.
class Human(models.Model):
    SEX = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=20, choices=SEX)

    def __str__(self) -> str:
        return f'{self.name}'