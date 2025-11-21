from src.coffee_machine import CoffeeMachine
from src.cash_operation import MoneyOperation

machine_is_on = True
machine = CoffeeMachine("Tets make", "Test model")

while machine_is_on:

    user_choice = input("'1' to see the list of drinks: \n"
                        "'2' to make a drink: \n"
                        "'3' to see the machine resources (for the maintainer): \n"
                        "'0' to turn off the machine (for the maintainer): \n")

    if user_choice == '1':
        drinks = machine.get_drinks()

        for drink in drinks:
            print(f"{drink.get('name')}: {drink.get('cost')}$")

    elif user_choice == '2':
        drink_name = input("Enter the drink you want: ")

        nominals = []

        print("The machine accepts only: 1 cent (0.01), 5 cent (0.05), 10 cent (0.1), 25 cent (0.25), 1$, 2$, 5$, 10$")
        print("To stop incerting, enter: 'stop'")

        while True:

            user_input = input("Enter the nominal: ")
                
            if user_input == 'stop':
                break

            try:
                value = float(user_input)
                nominals.append(value)

            except ValueError:
                print("Please enter only numeric values (or 'stop' to finish)")
        
        balance = MoneyOperation.receive_payment(nominals)

        if balance['success']:

            drink = machine.make_drink(drink_name, balance['balance'])

            if drink['success']:
                print(drink['message'])
                
                print(f"Here's your change: {drink['change']}") if drink['change'] > 0 else None
            else:
                print(drink['message'])
        else:
            print(balance['message'])

    elif user_choice == '3':
        resources = machine.get_machine_resourses()

        for resource in resources.get('resources'):
            print(f"{resource}: {resources.get('resources')[resource]}")

        print(f"balance: {resources.get('balance')}")

    elif user_choice == '0':
        machine.save_data_to_files()
        machine_is_on = False