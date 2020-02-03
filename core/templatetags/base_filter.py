from ..models import Menu, Settings, ModalMenu
from django import template


register = template.Library()


@register.simple_tag
def get_menus():
    return Menu.objects.filter(status=True)

@register.simple_tag
def get_modal_menus():
    return ModalMenu.objects.filter(status=True)



@register.simple_tag
def get_settings():
    return Settings.objects.last()



