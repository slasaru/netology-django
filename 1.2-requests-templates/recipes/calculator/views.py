from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home(request):
    return HttpResponse("Посмотрите на наши рецепты! <br/>Для этого введите в адресной строке блюда (omlet, pasta, buter). <br/>Если нужно больше одной порции, то добавьте количество servings")
    

def index(request):
    servings = int(request.GET.get("servings", 1))
    path_var = str(Path(request.path))[1:]
    context = {
               "recipe": DATA[path_var],
               "servings": servings,
               "path_var": path_var
               }
    return render(request, 'calculator/index.html', context)