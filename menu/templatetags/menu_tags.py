from django import template
from menu import models

register = template.Library()


@register.simple_tag()
def get_menu():
    menu_all = models.MenuItem.objects.filter(parent__isnull=True)
    return menu_all


@register.simple_tag()
def get_sub_menu(menu_name):
    menu_all = models.MenuItem.objects.filter(parent__isnull=True)
    return menu_all


