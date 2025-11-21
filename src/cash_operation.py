from src.drink import Drink
from typing import TypedDict

class PaymentResult(TypedDict):
    success: bool
    change: int | float

class MoneyOperation:

    AVAILABLE_NOMINALS = [0.01, 0.05, 0.1, 0.25, 1.0, 2.0, 5.0, 10.0]

    @classmethod
    def receive_payment(cls, nominals: list) -> dict:

        if len(nominals) == 0:
            return {
                "success": False,
                "message": "No money incerted",
                "balance": 0.0
            }

        for nominal in nominals:

            if nominal not in MoneyOperation.AVAILABLE_NOMINALS:
                return {
                    "success": False,
                    "message": f"The machine can't acceept: {nominal}. Money refunded",
                    "balance": 0.0
                }
        

        return {
            "success": True,
            "message": "The nominals are are valid",
            "balance": sum(nominals)
        }
        

    @classmethod
    def process_payment(cls, user_payment: float, drink: Drink) -> PaymentResult:
        
        if user_payment == drink.cost:
            return {
                "success": True,
                "change": 0
            }
        
        elif user_payment > drink.cost:
            return {
                "success": True,
                "change": user_payment - drink.cost
            }
        
        else:
            return {
                "success": False,
                "change": 0
            }

