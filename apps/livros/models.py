from django.db import models

class Livros(models.Model):

    id = models.AutoField(primary_key=True, db_column='id')
    nome = models.CharField(default='', null=True, blank=True, max_length=200)