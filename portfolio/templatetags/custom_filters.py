from django import template

register = template.Library()

@register.filter
def split_technologies(value, delimiter=','):
    return [v.strip() for v in value.split(delimiter)]