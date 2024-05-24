from django import template

register = template.Library()

@register.filter("mofo")
def mofo(value):
    return f"{value:,}"

@register.filter("discount")
def discount(price,dis):
    new = price - ((price * dis) / 100)
    if new == int(new):
        return int(new)
    return f"{new:.2f}"