from django.shortcuts import render

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
    'buter_super_puper': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 3,
        'сыр, ломтик': 2,
        'помидор, ломтик': 1,
    },
    'hotdog': {
        'сосиска, шт': 1,
        'кетчуп': 1,
        'булочка': 1,
    },
    'chifir': {
        'кипяток, кружка': 1,
        'чай, пачка': 1,
    },
    # можете добавить свои рецепты ;)
}


def show_menu(request):
    template = 'calculator/menu.html'
    context = {'recipes': DATA}
    return render(request, template, context)


def show_recipe(request, recipe):
    if request.method == "POST":
        servings = int(request.POST.get('servings', 1))
    else:
        servings = int(request.GET.get('servings', 1))
    template = 'calculator/index.html'
    recipe = DATA[recipe]
    servings_recipe = {}
    for ingredient, count in recipe.items():
        servings_recipe[ingredient] = count * servings
    context = {'recipe': servings_recipe, 'servings': servings}
    return render(request, template, context)
