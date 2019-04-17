from django import template

register = template.Library()

@register.simple_tag()
def get_tax(price, tax, *args, **kwargs):
    # you would need to do any localization of the result here

    price = int(price)
    total = price*tax
    return round(total,2)

@register.simple_tag()
def get_full_amount(price, tax, *args, **kwargs):
    # you would need to do any localization of the result here
    price = float(price)
    tax = (tax+1)
    # import pdb; pdb.set_trace()
    return round(price*tax,2)