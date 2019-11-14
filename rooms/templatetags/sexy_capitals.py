from django import template

register = template.Library()


@register.filter
def sexy_capitals(value):
    return value.capitalize()
