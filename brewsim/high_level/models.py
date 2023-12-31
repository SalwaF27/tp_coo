from django.db import models
from json import dumps

# Create your models here.
class Departement(models.Model):
        numero = models.IntegerField()
        prixparMcarre = models.DecimalField(max_digits=10, decimal_places=2)
        def __str__(self):
                return f"{self.numero} {self.prixparMcarre}"
        def json(self):
            return {"numero":self.numero, "prixparMcarre":float(self.prixparMcarre)}


class Machine(models.Model):
        nom = models.CharField(max_length=100)
        prix = models.IntegerField()
        def __str__(self):
                return f"{self.nom} {self.prix}"
        def costs(self):
                return self.prix
        def json(self):
                return {"nom":self.nom, "prix":self.prix}

class Ingredient(models.Model):
        nom = models.CharField(max_length=100)
        def __str__(self):
                return f"{self.nom}"
        def json(self):
                return {"nom":self.nom}

class QuantiteIngredient(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        quantite = models.IntegerField()
        def __str__(self):
                return f"{self.ingredient} {self.quantite}"
        def costs(self, departement):
            print(self.ingredient, departement)
            return self.ingredient.prix_set.get(departement__numero=departement).prix * self.quantite
        def json(self):
                return {"ingredient":self.ingredient.id, "quantite":self.quantite}

class Action(models.Model):
        machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
        commande = models.IntegerField()
        duree = models.IntegerField()
        ingredients = models.ManyToManyField(QuantiteIngredient)
        action = models.CharField(max_length=100)
        def __str__(self):
                return f"{self.machine} {self.commande} {self.duree} {self.ingredients} {self.action}"
        def json(self):
            return {"machine":self.machine.id, "commande":self.commande, "duree":self.duree, "ingredients":[m.id for m in self.ingredients.all()], "action":self.action}

class Recette(models.Model):
        nom = models.CharField(max_length=100)
        action = models.ForeignKey(Action, on_delete=models.PROTECT)
        def __str__(self):
                return f"{self.nom} {self.action}"
        def json(self):
            return {"nom":self.nom, "action":self.action.id}

class Usine(models.Model):
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        taille = models.IntegerField()
        machines = models.ManyToManyField(Machine)
        recettes = models.ManyToManyField(Recette)
        stocks = models.ManyToManyField(QuantiteIngredient)
        def  costMachines(self):
            total=0
            for m in self.machines.all():
                total= total + m.prix
            stock_total=0
            for m in self.stocks.all():
                stock_total= stock_total + m.costs(self.departement.numero)
            return total + stock_total
        def __str__(self):
                return f"{self.departement} {self.taille} {self.machines} {self.recettes} {self.stocks}"
        def costs(self):
                return (self.taille * self.departement.prixparMcarre ) + (self.costMachines())
        def json(self):
                return {"departement":self.departement.id, "taille":self.taille,
                "machines":[m.id for m in self.machines.all()], "recettes":[m.id for m in self.recettes.all()], "stocks":[m.id for m in self.stocks.all()]}


class Prix(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        prix = models.IntegerField()
        def __str__(self):
                return f"{self.ingredient} {self.departement} {self.prix}"
        def json(self):
                return{"ingredient":self.ingredient.id, "departement":self.departement.id, "prix":self.prix}

#Création des objets pour chaque classe

departement=Departement()
machine=Machine()
ingredient=Ingredient()
quantiteingredient=QuantiteIngredient()
action=Action()
recette=Recette()
usine=Usine()
prix=Prix()
