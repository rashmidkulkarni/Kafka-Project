from faker import Faker
from pizzaproducer import PizzaProvider

fake = Faker()
fake.add_provider(PizzaProvider)
def generate_pizza_details():
    pizza_details_list = []
    for i in range(30):
        pizza_details = {
            'name': fake.name(),
            'address': fake.address(),
            'phone': fake.phone_number(),
            'pizza': fake.pizza_name(),
            'quantity': fake.pizza_quantity()
        }
        pizza_details_list.append(pizza_details)
    return pizza_details_list
message={
    'name':fake.name(),
    'address':fake.address(),
    'phone':fake.phone_number()
}
print(message)