from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list("abcdefghijklpnomswzxqyu")

    uppercase = request.GET.get("uppercase")
    special_char = request.GET.get("special")
    numbers = request.GET.get("numbers")
    length = int(request.GET.get("length"))

    if uppercase:
        characters.extend("ABCDEFGHIJKLMNPOWZXYUQ")
    if special_char:
        characters.extend("%$#@!^&*~`/x")
    if numbers:
        characters.extend("1234567890")

    password = ""

    for i in range(length):
        password += random.choice(characters)

    
    return render(request, 'generator/password.html', {"password": password})

def about(request):
    return render(request, 'generator/about.html')


