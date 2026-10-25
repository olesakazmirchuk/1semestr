
import random


INGREDIENTS_POOL = {}

for i in range(1, 205):
    INGREDIENTS_POOL[f"Ingredient_{i}"] = random.randint(5, 20)


POTIONS_POOL = {}

for i in range(1, 51):
    POTIONS_POOL[f"Potion_{i}"] = random.randint(40, 150)


RECEPI = {}
ingredients_list = list(INGREDIENTS_POOL.keys())

for i in range(1, 51):
    ingredient_1 = ingredients_list[(i * 3) % len(ingredients_list)]
    ingredient_2 = ingredients_list[(i * 7) % len(ingredients_list)]

    if ingredient_1 == ingredient_2:
        ingredient_2 = ingredients_list[(i * 7 + 1) % len(ingredients_list)]

    RECEPI[f"Potion_{i}"] = [ingredient_1, ingredient_2]


WIN_ZOLOTO = 1000
MAX_DAYS = 10
DAILY_ING = 5
