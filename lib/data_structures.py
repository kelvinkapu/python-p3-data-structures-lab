spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [] 
    for food in spicy_foods:
        names.append(food["name"])
    return names 
    # print(names)
    # print(spicy_foods[0]["name"],spicy_foods[1]["name"],spicy_foods[2]["name"])

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spicy=[]
    for dictionary in spicy_foods:
        if dictionary["heat_level"]>5:
          spicy.append(dictionary)
          return spicy
print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print(print_spicy_foods(spicy_foods))
    # for food in spicy_foods:
        # print(food ["name"](food["cuisine"])|food["heat_level"]=="🌶")
        # spicy.append(food["name"]+food[("cuisine")]+"|")
        # print(spicy_foods[0]["name"]+(spicy_foods[0]["cuisine"]))
        # print(spicy_foods[1]["name"]+(spicy_foods[1]["cuisine"]))
        # print(spicy_foods[2]["name"]+(spicy_foods[2]["cuisine"]))
        # spicy_foods[1]["name"]
        # spicy_foods[2]["name"])



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
# print (get_spicy_food_by_cuisine(spicy_foods, cuisine))


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
           heat_level = "🌶" * food["heat_level"]
           print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    # spicy_food=[{"name":"", "cuisine":"","heat_level":""}]
    # for food in spicy_foods:
        spicy_foods.append(spicy_food)
        return spicy_foods
    # print(spicy_foods + spicy_food)