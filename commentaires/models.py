#from django.db import models
from djongo import models

class Commentaire(models.Model):
    id = models.ObjectIdField(db_column="_id", primary_key=True)
    commentaire = models.CharField(max_length=200,null=True)
    nature = models.CharField(max_length=100)
    key =  models.CharField(max_length=100)
    code =  models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    numero_ordre = models.CharField(max_length=100)

