from django.shortcuts import render, redirect
from .models import Cart, ProductTable
from order.models import Order
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from billing.models import BIllingProfile
from address.form import AddressForm
from address.models import Address


# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = ProductTable.objects.get(id=product_id)
        except ProductTable.DoesNotExist:
            print("show message to user,product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)  # if this view creates new cart go to cart home

    order_obj = None
    if cart_created or cart_obj.products.count() == 0:  # if this view creates new cart go to cart home
        return redirect("cart:home")
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get('billing_address_id', None)
    shipping_address_id = request.session.get('shipping_address_id', None)

    billing_profile, billing_profile_created = BIllingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session['billing_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save()

    if request.method == "POST":
        # checks the order us done
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session["cart_items"] = 0
            del request.session['cart_id']
            return redirect("cart:success")

    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'login_form': login_form,
        'guest_form': guest_form,
        'address_form': address_form,
        'address_qs ': address_qs
    }
    return render(request, "cart/checkout.html", context)


def checkout_doneView(request):
    return render(request, "cart/checkout-done.html",{})
