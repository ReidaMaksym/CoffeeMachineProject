from src.drink import Drink
from src.cash_operation import MoneyOperation
import json

def read_json_file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_name}'. Check for malformed JSON.")

    return data


class CoffeeMachine:

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.resources = CoffeeMachine.set_machine_resourses()
        self.drinks = CoffeeMachine.set_drinks()
        self.money_balance = CoffeeMachine.set_machine_cash_balance()


    @classmethod
    def set_drinks(cls) -> list[Drink]:

        drinks = []

        data = read_json_file("./data/drinks.json")
        
        for drink in data:
            new_drink = Drink(drink.get('name'), drink.get('cost'), drink.get('ingredients'))
            drinks.append(new_drink)
        
        return drinks


    @classmethod
    def set_machine_resourses(cls) -> dict:

        data = read_json_file('./data/machineResourses.json')
        return data
    

    @classmethod
    def set_machine_cash_balance(cls):
        data = read_json_file('./data/balance.json')
        return data.get('balance')


    def save_data_to_files(self):

        with open('./data/machineResourses.json', 'w') as file:
             json.dump(self.resources, file, indent=4)

        with open('./data/balance.json', 'w') as file2:
            data = {
                "balance": self.money_balance
            }
            json.dump(data, file2, indent=4)



    def get_machine_resourses(self) -> dict:
        return {
            "resources": self.resources,
            "balance": self.money_balance
        }
    
    
    def get_drinks(self) -> list[dict]:
        
        drinks = []

        for drink in self.drinks:
            drinks.append({
                "name": drink.name,
                "cost": drink.cost
            })
        
        return drinks
    

    def get_drink_by_name(self, drink_name: str) -> Drink | None:

        for drink in self.drinks:
            if drink_name == drink.name:
                return drink
        
        return None
    

    def is_resource_sufficient(self, drink: Drink) -> dict:

        for ingridient in self.resources:
            if self.resources[ingridient] < drink.ingridients[ingridient]:
                return {
                    "success": False,
                    "message": f"Can't make {drink.name}. Not enough of {ingridient}"
                }
        
        return {
            "success": True,
            "message": "Enough resources"
        }
    

    def make_drink(self, drink_name: str, payment: float) -> dict:

        drink = self.get_drink_by_name(drink_name)

        if not drink:
            return {
                "success": False,
                "message": f"Sorry, machine can't make '{drink_name}', money refunded"
            }
        
        resource_check = self.is_resource_sufficient(drink)

        if not resource_check['success']:
            return {
                "success": False,
                "message": f"{resource_check['message']}. Money refunded"
            }

        processed_payment = MoneyOperation.process_payment(payment, drink)

        if not processed_payment['success']:
            return {
                "success": False,
                "message": "Sorry, not enough money. Money refunded"
            }

        for ingridient in drink.ingridients:
            if drink.ingridients[ingridient] > 0:
                self.resources[ingridient] -= drink.ingridients[ingridient]
        
        self.money_balance += drink.cost

        return {
            "success": True,
            "message": f"Here is your {drink.name}, enjoy",
            "change": round(processed_payment['change'], 2) if processed_payment['change'] > 0 else 0.0
        }

                

