from django import template
from ..models import HtmlContent

register = template.Library()

@register.filter(is_safe=True)
def html_content(keyword):
    hc =  HtmlContent.objects.filter(keyword=keyword)
    if hc.count() == 1:
        return hc[0].content

    return keyword
