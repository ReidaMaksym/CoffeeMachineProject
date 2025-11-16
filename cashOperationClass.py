from drinkClass import Drink
from typing import TypedDict

class PaymentResult(TypedDict):
    make_coffee: bool
    change: int | float

class MoneyOperation:

    @classmethod
    def receive_payment(cls) -> float | int:
        
        print("The machine accepts only: 1 cent (0.01), 5 cent (0.05), 10 cent (0.1), 25 cent (0.25), 1$, 2$, 5$, 10$")

        dollar_and_cents_nominals = [0.01, 0.05, 0.1, 0.25, 1.0, 2.0, 5.0, 10.0]

        balance = 0
        inserting_money = True

        while inserting_money:
            
            try:

                payment = float(input("Inset bill or coin: "))
                
                if payment in dollar_and_cents_nominals:
                    balance += payment
                    print("Processed...")
                    print(f"You incerted {balance}")

                    stop_incetring = input("To stop incerping, type 'stop', to 'continue': ").lower()

                    if stop_incetring == 'stop':
                        inserting_money = False
                else:
                    print(f"Sorry, the machine can't process {payment}")
                
            except ValueError:
                print("Machine can't process your nominal, try again")
        
        return balance
    

    @classmethod
    def process_payment(cls, user_payment: float, drink: Drink) -> PaymentResult:
        
        if user_payment == drink.cost:
            return {
                "make_coffee": True,
                "change": 0
            }
        
        elif user_payment > drink.cost:
            return {
                "make_coffee": True,
                "change": user_payment - drink.cost
            }
        
        else:
            return {
                "make_coffee": False,
                "change": 0
            }

