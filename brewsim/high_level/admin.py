from django.contrib import admin

# Register your models here.
from.models import Departement, Machine, Ingredient, QuantiteIngredient, Action, Recette, Usine, Prix

admin.site.register(Departement)
admin.site.register(Machine)
admin.site.register(Ingredient)
admin.site.register(QuantiteIngredient)
admin.site.register(Action)
admin.site.register(Recette)
admin.site.register(Usine)
admin.site.register(Prix)
