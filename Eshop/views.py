from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers, viewsets

from .serializers import UserSerializer


def index(request):
    if request.method == "POST":
        product_id = request.POST.get('cart_id')
        cart_id = request.session.get('cart')
        remove = request.POST.get('minus')

        #print(".....", cart_id)
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:

                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session['cart'] = cart_id
        #print(".....request.session['cart']", request.session['cart'])

    cate = category.objects.all()

    cate_id = request.GET.get('category_id')
    if cate_id:
        pro = Product.objects.filter(category=cate_id)
    else:
        pro = Product.objects.all()

    context = {
        'category': cate,
        'pro': pro
    }
    return render(request, 'home.html', context=context)


def SignIn(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email_id = request.POST.get('email')
        password = request.POST.get('pwd')
        mobile = request.POST.get('mbl')
        gender = request.POST.get('gender')

        save_info = signup(firstname=first_name, lastname=last_name, email=email_id,
                           password=make_password(password), mobile=mobile, gender=gender)
        save_info.save()

        return redirect('home')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            fetchObj = signup.objects.get(email=email)
            if check_password(password, fetchObj.password):
                request.session['name'] = fetchObj.firstname
                request.session['email'] = fetchObj.email
                request.session['customer_id'] = fetchObj.id
                return redirect('home')
            else:
                return HttpResponse('password is wrong')
        except:
            return HttpResponse("Wrong Email")


def logout(request):
    request.session.clear()
    return redirect('home')


def cart_info(request):
    cart_id = request.session.get('cart').keys()
    filtered_product = Product.objects.filter(id__in=cart_id)

    return render(request, 'cart.html', {'filtered_product': filtered_product})


def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse('Please Login')
        cart = request.session.get('cart')
        product = Product.objects.filter(id__in=list(cart.keys()))
        for pro in product:
            price = pro.price

            order_info = order_dtls(address=address, mobile=mobile, customer=signup(
                id=customer_id), product=pro, price=price, quantity=cart.get(str(pro.id)))
            order_info.save()

        request.session['cart'] = {}
    return redirect('cart')


def ord_info(request):
    customer_id = request.session.get('customer_id')
    fetch_order = order_dtls.objects.filter(customer=customer_id)

    tp = 0
    for pro in fetch_order:
        tp = tp + (pro.price * pro.quantity)

    return render(request, 'order.html', {'fetch_order': fetch_order, 'tp': tp})


class UserViewSet(viewsets.ModelViewSet):
    queryset = signup.objects.all()
    serializer_class = UserSerializer
