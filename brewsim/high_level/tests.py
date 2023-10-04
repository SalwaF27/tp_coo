from django.test import TestCase

from .models import Machine, Departement, Usine, QuantiteIngredient, Prix, Ingredient, Recette, Action



class Tests(TestCase):
    def test_cost(self):

        departement=Departement.objects.create(numero=31, prixparMcarre=2000 )
        usine=Usine.objects.create(taille=50 ,departement=departement)
        houblon=Ingredient.objects.create(nom="houblon")
        orge=Ingredient.objects.create(nom="orge")
        stock_houblon=QuantiteIngredient.objects.create(ingredient=houblon, quantite=50)
        stock_orge=QuantiteIngredient.objects.create(ingredient=orge, quantite=100)

        Four=Machine.objects.create(nom="Four", prix=1000)
        Lave_vaisselle=Machine.objects.create(nom="Lave_vaisselle", prix=2000)

        usine.machines.add(Four)
        usine.machines.add(Lave_vaisselle)
        usine.stocks.add(stock_houblon)
        usine.stocks.add(stock_orge)

        self.assertEqual(Usine.objects.count(), 1)

        Prix.objects.create(ingredient=houblon, departement=departement, prix=20)
        Prix.objects.create(ingredient=orge, departement=departement, prix=10)

        cost_f= 105000
        self.assertEqual(usine.costs(), cost_f)
