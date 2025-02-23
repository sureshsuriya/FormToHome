from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import Seller  
# from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User
from .models import Products,Order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def home(request):
    return render(request, 'Homepage.html')

def register_seller(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
    
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register_seller")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register_seller")
        else:
            create_user =  User.objects.create_user(username=username, email=email, password=password)
            create_user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("sell")

    return render(request, "register.html")

# def authenticate_seller(username, password):
#     """Custom authentication function for sellers."""
#     try:
#         seller = User.objects.get(username=username)
#         if check_password(password, seller.password):
#             return seller
#     except User.DoesNotExist:
#         return None

# def login_seller(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('orders')
#         else:
#             messages.error(request, 'Enter a Valid Username or Password.')

#     return render(request, 'sell.html')

def logout_view(request):
    if 'seller_id' in request.session:
        del request.session['seller_id']
    messages.success(request, 'Logged out successfully!')
    return redirect('login_seller')

# def orders(request):
#     return render(request, 'orders.html')
def buy(request):
    products = Products.objects.all()
    return render(request, 'buy.html', {'products': products})

def sell(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('seller_product_details')
        else:
            messages.error(request, 'Enter a Valid Username or Password.')

    return render(request, 'sell.html')

# def seller_product_details(request):
#     return render(request, 'order_details.html')


def seller_product_details(request):
    if request.method == 'POST':
        product_name = request.POST.get('product-name')
        price = request.POST.get('price')
        contact = request.POST.get('contact')
        description = request.POST.get('description')
        location = request.POST.get('location')
        product_image = request.FILES.get('product_image')
        available_kg = request.POST.get('available_kg')  # Get available kg from form

        product = Products(
            product_name=product_name,
            price=price,
            contact=contact,
            description=description,
            location=location,
            product_image=product_image,
            available_kg=available_kg  # Save available kg to database
        )
        product.save()
        messages.success(request, 'Product added successfully!')

    products = Products.objects.all()
    return render(request, 'order_details.html', {'products': products})




def delete_order(request, order_id):
    product = get_object_or_404(Products, id=order_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    
    # Fetch updated product list
    products = Products.objects.all()
    return render(request, 'order_product_details.html', {'products': products})


def order_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('order_register')

        # Use Django's create_user for password hashing
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('order_login')

    return render(request, 'register_order.html')

def order_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            orders = Order.objects.all()  # Fetch orders instead of products
            return render(request, 'order_product_details.html', {'orders': orders})  # Pass orders to the template
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('order_login')

    return render(request, 'login_order.html')

# def buy(request):
#     products = Products.objects.all()
#     return render(request, 'buy.html', {'products': products})

def buy_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        contact_number = request.POST.get('contact_number')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        quantity = int(request.POST.get('quantity'))

        # Create a new order
        order = Order.objects.create(
            product=product,
            customer_name=customer_name,
            customer_email=customer_email,
            contact_number=contact_number,
            street_address=street_address,
            city=city,
            state=state,
            postal_code=postal_code,
            quantity=quantity
        )

        # Update the available kg of the product
        product.available_kg -= quantity
        product.save()

        messages.success(request, 'Order placed successfully!')
        return redirect('thank_you', order_id=order.id)

    return render(request, 'buy_product.html', {'product': product})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        delivery_option = request.POST.get('delivery_option')
        order.delivery_option = delivery_option
        order.save()
        messages.success(request, 'Delivery option selected successfully!')
        return redirect('home')
    return render(request, 'order_confirmation.html', {'order': order})
    return redirect('home')

def thank_you(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        delivery_option = request.POST.get('delivery_option')
        order.delivery_option = delivery_option  # Save delivery option to the database
        order.save()

        if delivery_option == 'deliver':
            messages.success(request, 'Your order will be delivered to your address!')
        else:
            messages.success(request, 'You can come to our location to pick up your order!')

    return render(request, 'thank.html', {'order': order})
def order_product_details(request):
    orders = Order.objects.all()
    return render(request, 'order_product_details.html', {'orders': orders})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_product_details')

def sold_product_details(request):
    products = Products.objects.all()
    return render(request, 'sold_product_details.html', {'products': products})

def edit_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        product.product_name = request.POST.get('product_name')
        product.price = request.POST.get('price')
        product.contact = request.POST.get('contact')
        product.description = request.POST.get('description')
        product.location = request.POST.get('location')
        product.available_kg = request.POST.get('available_kg')
        if request.FILES.get('product_image'):
            product.product_image = request.FILES.get('product_image')
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('sold_product_details')
    return render(request, 'edit_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('sold_product_details')

# def buy(request, product_id):
#     product = get_object_or_404(Products, id=product_id)  # Fetch product
#     return render(request, 'buy_product.html', {'product': product})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        delivery_option = request.POST.get('delivery_option')
        order.delivery_option = delivery_option
        order.save()
        messages.success(request, 'Delivery option selected successfully!')
        return redirect('home')
    return render(request, 'order_confirmation.html', {'order': order})


def buy_view(request):
    products = Products.objects.all()  # Fetch all products from MongoDB
    return render(request, 'buy.html', {'products': products})
    

from django.shortcuts import render
from .models import Products

def product_list(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'buy_product_detail.html', {'product': product})

def buy_product(request, product_id):  # Using product_id
    if request.method == 'POST':
        product = get_object_or_404(Products, id=product_id)  # Fetch using product_id
        order = Order(
            product=product,
            quantity=request.POST.get('quantity'),
            customer_name=request.POST.get('customer_name'),
            customer_email=request.POST.get('customer_email'),
            contact_number=request.POST.get('contact_number'),
            street_address=request.POST.get('street_address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            postal_code=request.POST.get('postal_code'),
            delivery_option=request.POST.get('delivery_option')
        )
        order.save()
        return redirect('thank-you', order_id=order.id)

    return redirect('product-detail', id=product_id)  # Updated to match parameter name


def thank_you(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        delivery_option = request.POST.get('delivery_option')
        order.delivery_option = delivery_option  # Save delivery option to the database
        order.save()

        if delivery_option == 'deliver':
            messages.success(request, 'Your order will be delivered to your address!')
        else:
            messages.success(request, 'You can come to our location to pick up your order!')

    return render(request, 'thank.html', {'order': order})