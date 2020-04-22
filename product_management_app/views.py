from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Deal, OrderItem
from login_app.models import UserProfile
from datetime import datetime
from django.core import serializers


@login_required
def index(request):
    # Get all products but only first time
    if 'products' in request.session:
        products = [des_product.object for des_product in serializers.deserialize('json', request.session['products'])]
        print(products)
    else:
        products = Product.objects.filter().order_by('name')
        request.session['products'] = serializers.serialize('json', products)

    # Get all deals but only first time
    if 'deals' in request.session:
        deals = [des_deal.object for des_deal in serializers.deserialize('json', request.session['deals'])]
    else:
        today_date = datetime.today().strftime('%Y-%m-%d')
        deals = Deal.objects.filter(start_date__lte=today_date,
                                    end_date__gte=today_date)
        request.session['deals'] = serializers.serialize('json', deals)

    # Get all cart_items in session['cart'] if exists
    if 'cart' in request.session:
        cart = [des_cart_item.object for des_cart_item in serializers.deserialize('json', request.session['cart'])]
    else:
        cart = None

    context = {'products': products,
               'deals': deals,
               'cart': cart}
    return render(request, "product_management_app/index.html", context)


@login_required
def add_product_to_cart(request):
    if 'product_id' not in request.POST:
        return HttpResponseRedirect(reverse('product_management_app:shopping'))
    # Get submitted product
    product = Product.objects.get(pk=request.POST['product_id'])

    # Initialize order and add to session if not exists
    if 'order' not in request.session:
        order = Order()
        request.session['order'] = serializers.serialize('json', [order])
    else:
        order = next(serializers.deserialize('json', request.session['order'])).object

    order_item = OrderItem()
    order_item.product = product
    order_item.order = order

    # If there is no cart in session
    if 'cart' not in request.session:
        order_item.quantity = 1
        cart = serializers.serialize('json', [order_item])
        request.session['cart'] = cart

    # If the cart has been initialized and added to session
    else:
        cart = [des_cart_item.object for des_cart_item in serializers.deserialize('json', request.session['cart'])]
        # If product does not exist in cart append it
        if product not in [cart_item.product for cart_item in cart]:
            order_item.quantity = 1
            cart.append(order_item)
        # If product exists in cart then add 1 to quantity
        else:
            for cart_item in cart:
                if cart_item.product == product:
                    cart_item.quantity += 1
        request.session['cart'] = serializers.serialize('json', cart)

    return HttpResponseRedirect(reverse('product_management_app:shopping'))


