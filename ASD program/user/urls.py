from django.urls import path

from user import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("register", views.register, name = "register"),
    path("login", views.loginfunction, name = "login"),
    path("logout", views.logoutfunction, name = "logout"),
    path("add_sale", views.addSale, name = "add_sale"),
    path("buy_sale", views.buySale, name = "buy_sale"),
    path("confirmation_screen/<int:pk>", views.confirmationScreen, name = "confirmation_screen"),
    path('post/<str:pk>', views.post, name = "post")    # A variable called "pk", which is a string variable. This can be used to make a dynamic URL
]