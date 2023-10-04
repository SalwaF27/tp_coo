from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Departement, Machine, Usine, Recette, Prix, QuantiteIngredient, Ingredient, Action
from json import dumps


class DepartementDetailView(DetailView):
        model=Departement
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))

class MachineDetailView(DetailView):
        model=Machine
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))


class IngredientDetailView(DetailView):
        model=Ingredient
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))

class QuantiteIngredientDetailView(DetailView):
        model=QuantiteIngredient
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))

class ActionDetailView(DetailView):
        model=Action
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))

class RecetteDetailView(DetailView):
        model=Recette
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))

class UsineDetailView(DetailView):
        model=Usine
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))


class PrixDetailView(DetailView):
        model=Prix
        def render_to_response(self, context, **response_kwargs):
            return HttpResponse(dumps(self.object.json()))
