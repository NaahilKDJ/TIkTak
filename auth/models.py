from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_lenght=100)
    password = models.CharField(max_lenght=150)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    dateDeNaissance = models.DateField()
    dateCreationCompte = models.DateField()
    private = models.BooleanField(default=True)
    profilePic = models.FileField()



    def __str__(self):
        return f"{self.nom} {self.prenom} né le {self.dateDeNaissance}"
