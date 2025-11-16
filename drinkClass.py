
class Drink:

    def __init__(self, name: str, cost: float, ingridients: dict[str, int]):
        self.name = name
        self.cost = cost
        self.ingridients = ingridients
    
    def __str__(self) -> str:
        return f"{self.name}: {self.cost}$"
    
    def __repr__(self) -> str:
        return f"<Drink: name: {self.name}, cost:{self.cost}>"
    

