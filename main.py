from pprint import pprint
import json
import ast

with open(file="recipes.txt", mode="r") as file:
    info = file.read()
    cook_book = {}
    splitted_data = info.split("\n" * 2)

    for dish in splitted_data:
        dish_item = dish.split("\n")
        dish_name = dish_item[0]
        ingridients_number = dish_item[1]
        ingridients = dish_item[2:]
        ingridient_list = []
        products = {}

        for product in ingridients:
            element = product.split("|")
            product_name = element[0]
            product_volume = element[1]
            product_measurement = element[2]
            products = {"ingredient_name": product_name, "quantity": product_volume, 'measure': product_measurement}
            ingridient_list.append(products)

        cook_book.setdefault(dish_name, ingridient_list)

pprint(cook_book)

with open(file="dishes.txt", mode="w") as file_object:
    json.dump(cook_book, file_object, skipkeys=False, ensure_ascii=False, indent=None)

class Dishes_to_cook:
    def __init__(self, dishes):
        self.dishes = dishes

    def get_shop_list_by_dishes(meals, persons_count):
        with open(file="dishes.txt", mode="r") as file:
            data = file.read()
            cook_book = ast.literal_eval(data)
            shop_list_by_dishes = []
            for meal in meals:
                for recipe in cook_book.keys():
                    if meal == recipe:
                        ingredient_to_buy = {}
                        for ingredient in cook_book[recipe]:
                            ingredient_count = ingredient['quantity'] * persons_count
                            ingredient_to_buy = {"Product: ": ingredient['ingredient_name'], "Quantity: ": ingredient_count}
                            shop_list_by_dishes.append(ingredient_to_buy)
        return (shop_list_by_dishes)

meals = ['Запеченный картофель', 'Омлет']
persons_count = int(input("Введите количество персон: "))
print(Dishes_to_cook.get_shop_list_by_dishes(meals, persons_count))