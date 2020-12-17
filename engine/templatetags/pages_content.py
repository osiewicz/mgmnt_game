from django import template

register = template.Library()

@register.filter(is_safe=True)
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0.0

