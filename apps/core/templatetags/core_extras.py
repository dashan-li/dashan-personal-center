from django import template

register = template.Library()


@register.filter(name='split')
def split_filter(value, delimiter=','):
    """Split a string by a delimiter."""
    return [item.strip() for item in str(value).split(delimiter) if item.strip()]


@register.filter(name='strip')
def strip_filter(value):
    """Strip whitespace from a string."""
    return str(value).strip()
