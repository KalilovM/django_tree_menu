from django import template
from ..models import MenuItem
from django.utils.html import mark_safe
from django.utils.safestring import SafeString

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True).order_by('ordering')
    menu_html = SafeString('<ul>')

    for item in menu_items:
        menu_html += SafeString('<li>')
        menu_html += SafeString(f'<a href="{item.url}">{item.name}</a>')
        menu_html += draw_submenu(item)
        menu_html += SafeString('</li>')

    menu_html += SafeString('</ul>')
    return mark_safe(menu_html)


def draw_submenu(parent_item):
    submenu_items = MenuItem.objects.filter(parent=parent_item).order_by('ordering')
    if not submenu_items:
        return SafeString('')

    submenu_html = SafeString('<ul>')
    for item in submenu_items:
        submenu_html += SafeString('<li>')
        submenu_html += SafeString(f'<a href="{item.url}">{item.name}</a>')
        submenu_html += draw_submenu(item)
        submenu_html += SafeString('</li>')
    submenu_html += SafeString('</ul>')
    return mark_safe(submenu_html)
