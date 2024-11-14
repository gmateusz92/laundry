from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Pobiera wartość z słownika na podstawie klucza."""
    return dictionary.get(key)