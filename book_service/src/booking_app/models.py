from django.db import models

class Person(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    email = models.EmailField(null=True)  # Добавлено поле email
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Hotel(models.Model):
    name = models.CharField(max_length=40)
    stars = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name
