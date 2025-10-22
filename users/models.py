from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from users.validators import validate_cpf

class User(AbstractUser):
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])    
    amount = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    
    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)
        
    def pay(self, value:Decimal):
        if not isinstance(value, Decimal):
            raise TypeErrorError("O valor deve ser do tipo Decimal")
        self.amount -= value
        
    def recive(self, value:Decimal):
        if not isinstance(value, Decimal):
            raise TypeError("O valor deve ser do tipo Decimal")
        self.amount += value
        
    def __str__(self):
        return self.username
