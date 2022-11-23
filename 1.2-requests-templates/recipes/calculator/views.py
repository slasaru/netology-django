from django.shortcuts import render
from django.http import HttpResponse

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
}

def home(request):
    return HttpResponse("Посмотрите на наши рецепты! <br/>\
        Для этого введите в адресной строке блюда (например, omlet, pasta, buter).\
            <br/>Если нужно больше одной порции, то добавьте количество servings")
    

def index(request, dish):
    servings = int(request.GET.get("servings", 1))
    context = {}
    try:
        dish_dict = {ingredient: amount * servings for ingredient, amount in DATA[dish].items()}
        context = {"recipe": dish_dict,
                "servings": servings,
                "dish": dish}
    except KeyError:
        context = {"recipe": "?",
                "servings": servings,
                "dish": dish}
    return render(request, 'calculator/index.html', context)