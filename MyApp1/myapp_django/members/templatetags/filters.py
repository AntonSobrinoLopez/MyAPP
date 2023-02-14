from django import template

register = template.Library()

@register.filter
def lookup(diccionary, key):
    return diccionary.get(key)