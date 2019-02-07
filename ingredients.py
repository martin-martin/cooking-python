# CLASSES AND OBJECT-ORIENTED PROGRAMMING


class Ingredient:
    """Models an ingredient including its name and amount."""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"There are {self.amount} of {self.name}."

    def use(self, use_amount):
        """Reduces the amount of ingredient available."""
        self.amount -= use_amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name


# INHERITANCE: build a subclass called Spice


class Spice(Ingredient):
    # customize the __init__() method
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    # create a custom method grind()
    def grind(self):
        print(f"you have now {self.amount} of ground {self.name}")

    # override the expire() method
    def expire(self):
        if self.name == 'salt':
            print(f"{self.name} never expires! ask the sea!")
        else:
            print(f"this {self.name} went bad...")
            self.name = f"expired {self.name}"


# Here is the code to create a Soup object with the functionality shown in the video
class Soup:
    """Represents a soup that can get cooked from an ingredient list."""
    def __init__(self, ingredients_list):
        self.ingredients_list = ingredients_list
        self.name = ""
        self.num_ingredients = len(ingredients_list)
        self.serves = 0

    def cook(self):
        """Prepares the Soup object by using the ingredients and calculating the servings."""
        total_amount = 0
        for ingredient in self.ingredients_list:
            self.name += ingredient.name
            total_amount += ingredient.amount
        self.serves = total_amount / self.num_ingredients

    def __str__(self):
        return f"""Here's some yummy\n
{self.name}-
,adPPYba,  ,adPPYba,  88       88 8b,dPPYba,
I8[    "" a8"     "8a 88       88 88P'    "8a
 `"Y8ba,  8b       d8 88       88 88       d8
aa    ]8I "8a,   ,a8" "8a,   ,a88 88b,   ,a8"
`"YbbdP"'  `"YbbdP"'   `"YbbdP'Y8 88`YbbdP"'
                                  88
                                  88
serves {self.serves}."""
