from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

class MenuList(generic.ListView):
    # names for variable are set by Django
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # prevents starting with empty dictionary
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"