from django.shortcuts import render

def hotel(request):
    return render(request, 'hotel.html')


def about_us(request):
    return render(request, 'about_us.html')


def house_big(request):
    return render(request, 'house_big.html')


def house_small(request):
    return render(request, 'house_small.html')


def intertaiment(request):
    return render(request, 'intertaiment.html')

def contact(request):
    return render(request, 'contact.html')