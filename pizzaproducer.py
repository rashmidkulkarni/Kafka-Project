import random
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def pizza_name(self):
        valid_pizza_names = ['Margherita',
                             'Marinara',
                             'DoubleCheese',
                             'Chicken',
                             'Salami',
                             'Farmhouse']
        return valid_pizza_names[random.randint(0,len(valid_pizza_names)-1)]
    def pizza_quantity(self):
        return random.randint(1,5)