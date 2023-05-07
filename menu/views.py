from django.shortcuts import render
from django.views import View
from . import models


class Home(View):
    template_name = "menu/home.html"

    def get(self, request):
        return render(request, self.template_name)


class Menu(View):
    template_name = "menu/menu.html"

    def get(self, request, name):
        menu_item = models.MenuItem.objects.get(name=name)
        menu = models.MenuItem.objects.filter(tree_id=menu_item.tree_id, lft__gt=menu_item.lft, rght__lt=menu_item.rght)
        context = {"name": name, "menu": menu}
        return render(request, self.template_name, context=context)
