from django.db import models

# Create your models here.
class Departement(models.Model):
        numero = models.IntegerField()
        prixparMcarre = models.DecimalField(max_digits=10, decimal_places=2)

class Machine(models.Model):
        nom = models.CharField(max_length=100)
        prix = models.IntegerField()

class Ingredient(models.Model):
        nom = models.CharField(max_length=100)

class QuantiteIngredient(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        quantite = models.IntegerField()

class Action(models.Model):
        machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
        commande = models.IntegerField()
        duree = models.IntegerField()
        ingredients = models.ManyToManyField(QuantiteIngredient)
        action = models.CharField(max_length=100)

class Recette(models.Model):
        nom = models.CharField(max_length=100)
        action = models.ForeignKey(Action, on_delete=models.PROTECT)

class Usine(models.Model):
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        taille = models.IntegerField()
        machines = models.ManyToManyField(Machine)
        recettes = models.ManyToManyField(Recette)
        stocks = models.ManyToManyField(QuantiteIngredient)

class Prix(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        prix = models.IntegerField()
