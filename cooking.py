with open("recipe.txt", "r") as file_in:
    recipe = file_in.read()

lines = recipe.split('\n')

# FOR LOOP
ingredients = []
for item in lines:
    ingr = item.split()
    ingredients.append(ingr)

# DICTIONARY
ing_dict = {}
for ingredient in ingredients:
    amount = ingredient[0]
    name = ingredient[1]
    ing_dict[name] = int(amount)

print(ing_dict)
print(ing_dict['carrots'])


# FUNCTIONS
def clean(dictionary):
    """Removes items from a dictionary if their value is 0."""
    temp_dict = dictionary.copy()
    # look at each key, value pair
    for key, value in dictionary.items():
        # CONDITIONALS
        # if the value is 0, then remove the entry
        if value == 0 or key == 'snakes':
            temp_dict.pop(key)
        elif value < 0:
            temp_dict.pop(key)
    # give the resulting dictionary back as an output
    return temp_dict


new_dict = clean(ing_dict)
print(f"original dict: {ing_dict} is very long")
print(f"this: {new_dict} is the new dict!")
