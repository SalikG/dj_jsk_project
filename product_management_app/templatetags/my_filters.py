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


@register.filter
def get_price_sum_from_cart_and_deals(value, arg):
    cart = value
    deals = arg
    result = 0
    print(deals)
    for order_item in cart:
        print(order_item.product)
        one_product_price_sum = 0
        for deal in deals:
            if deal.product == order_item.product:
                one_product_price_sum = (order_item.product.price * order_item.quantity) * (1 - (deal.discount_persentage / 100))

        if one_product_price_sum == 0:
            one_product_price_sum = order_item.product.price * order_item.quantity

        result += one_product_price_sum

    return result



