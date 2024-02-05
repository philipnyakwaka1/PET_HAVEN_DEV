from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'State({self.name})'


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'City({self.name})'
