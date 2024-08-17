import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "index.html")

def game(request):
    num1 = random.randint(0, 3)
    num2 = random.randint(0, 3)
    num3 = random.randint(0, 3)
    if num1 == num2 == num3:
        response = f"Победа, все 3 числа равны! Числа: {num1}, {num2}, {num3}"
    else:
        response = f"Повезет в следующий раз! Числа: {num1}, {num2}, {num3}"
    return HttpResponse(response)

def get_phrase1(req):
    return HttpResponse("Первая фраза")

def get_phrase2(req):
    return HttpResponse("Вторая фраза")

def contact(req):
    print(req.POST.get("name"))
    print(req.POST.get("email"))
    print(req.POST.get("msg"))
    return HttpResponse("Форма успешно отправлена")