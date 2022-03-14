from ASD_program.settings import TEMPLATES
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from sale.models import Sales
from user.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

current_user_logged_in_username = ""

def index(request):
    '''Shows the main page'''

    '''namesList = o.get_names()

    rng = randint(3)

    name = namesList[rng]'''

    # To send data to the template files, the format is '{"key": value}'. In the HTML file, the format to use said data is '{{key}}'

    '''name = "Beepo"
       return render(request, 'index.html', {'name': name})
    '''

    # A dictionary can be used to send multiple data

    '''
    context = {
        "name": "Beepo",
        "age": "21",
        "nationality": "British",
    }

    return render(request, 'index.html', context)
    '''
    sale = Sales.objects.all()

    return render(request, 'index.html', {'sales': sale})

    # To add multiple variables, it can be done by adding more key/value to the brackets; like: "{'feature1': feature1,
    # 'feature2': feature2, ..., 'featureN': featureN}. Ideally, it would be better to use list"

def register(request):
    '''The view to create a new user'''

    if request.method == 'POST':
        email = request.POST.get('email', 'Placeholder')

        username = request.POST.get('username', 'Placeholder')
    
        password = request.POST.get('password', 'Placeholder')

        password2 = request.POST.get('password2', 'Placeholder2')

        if password == password2:

            if User.objects.filter(email = email).exists():
                messages.info(request, 'Este correo ya existe')

                return redirect('register')

            elif User.objects.filter(username = username).exists():
                messages.info(request, 'El usuario ya existe')

                return redirect('register')

            else:
                User.objects.create_user(email, username, password)

                return redirect('login')

        else:
            messages.info(request, "La contraseña no es igual")

            return redirect('register')

    else:
        return render(request, 'register.html')

def loginfunction(request):
    '''The view to sign in'''

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email = email, password = password)

        if user is not None:
            login(request, user)

            global current_user_logged_in_username

            current_user_logged_in_username = user.__str__()

            return redirect('/')

        else:
            messages.info(request, "Los datos no son correctos")

            return redirect('login')

    else:
        return render(request, 'login.html')

def logoutfunction(request):
    '''The function for a user to log out'''

    logout(request)

    return redirect('/')

def addSale(request):
    '''The function for a user to create and add a sale'''

    if request.method == "POST":
        type = request.POST.get('type', "")
        price = request.POST.get('price', "")

        if str.lower(type) == "compra" or str.lower(type) == "venta":
            username = current_user_logged_in_username

            print(current_user_logged_in_username)

            Sales.objects.add_sale(type, price, username)

            return redirect('/')

        else:
            messages.info(request, "El tipo de oferta debe ser 'Compra' o 'Venta'")

            return redirect('add_sale')

    else:
        return render(request, 'add_sale.html')

def buySale(request):
    '''The function for a user to buy/interact with a sale'''

    if request.method == "POST":
        return redirect('buy_sale')

    else:
        sale = Sales.objects.all()

        return render(request, 'buy_sale.html', {'sales': sale})

def confirmationScreen(request, pk = None):
    '''The function for a user to get the confirmation of the transaction'''
    
    Sales.objects.filter(id = pk).delete()

    return render(request, 'confirmation_screen.html')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})