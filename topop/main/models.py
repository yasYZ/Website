from django.db import models

# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return (f'{self.name} {self.email} {self.message}')


class login_account(models.Model):
    nameA = models.CharField(max_length=20)
    emailA = models.EmailField(max_length=100)
    passwordA = models.CharField(max_length=500)

    def __str__(self):
        return (f'{self.nameA}  {self.emailA}  {self.passwordA}')


class Plans(models.Model):
    nameP = models.CharField(max_length=20)
    emailP = models.EmailField(max_length=100)
    passwordP = models.CharField(max_length=500)

    def __str__(self):
        return (f'{self.nameP}  {self.emailP}  {self.passwordP}')
