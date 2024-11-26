from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    bank_account_number = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = ('firstname', 'lastname', 'date_of_birth')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
