from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

class Products(models.Model):
    categories = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=14, decimal_places=2)
    desctiption = models.TextField()
    amount = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.name}, {self.categories}'