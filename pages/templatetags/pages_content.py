from django import template
from ..models import HtmlContent

register = template.Library()

@register.filter(is_safe=True)
def html_content(keyword):
    hc =  HtmlContent.objects.filter(keyword=keyword)
    if hc.count() == 1:
        return hc[0].content

    return keyword

@register.filter(is_safe=True)
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return 0.0

