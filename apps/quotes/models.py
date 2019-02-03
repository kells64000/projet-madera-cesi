from django.db import models


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
