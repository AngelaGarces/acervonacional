from django.db import models

# Create your models here.
class livros(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    nome = models.CharField(default='', max_length= 200)