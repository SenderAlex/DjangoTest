from django.db import models

class Goat(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    scores = models.IntegerField()
    clubs = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.scores}, {self.clubs}'

    class Metta:
        verbose_name = 'Лучшие бомбардиры за всю историю Лиги Чемпионов'
        verbose_name_plural = 'Лучшие бомбардиры за всю историю Лиги Чемпионов'
