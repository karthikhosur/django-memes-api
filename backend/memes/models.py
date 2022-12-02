from django.db import models

# Create your models here.


class Subscribers(models.Model):
    email_id = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Subscribers"
        db_table = 'subscribers'
