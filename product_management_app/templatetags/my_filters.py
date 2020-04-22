from django import template

register = template.Library()


@register.filter
def sub_discount(value, arg):
    result = value - (value * (arg/100))
    return result


@register.filter
def get_deal(value, arg):
    deals = arg
    product = value
    result = next((deal for deal in deals if deal.product == product), None)
    return result


@register.filter
def get_quantity_price_with_deal(value, arg):
    order_item = value
    deal = arg
    result = (order_item.product.price * order_item.quantity) * (1 - (deal / 100))
    return result


