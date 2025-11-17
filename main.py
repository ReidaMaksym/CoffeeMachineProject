from src.coffeeMachineClass import CoffeeMachine

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

        machine.make_drink(drink_name)

    elif user_choice == '3':
        resources = machine.get_machine_resourses()

        for resource in resources.get('resources'):
            print(f"{resource}: {resources.get('resources')[resource]}")

        print(f"balance: {resources.get('balance')}")

    elif user_choice == '0':
        machine.save_data_to_files()
        machine_is_on = False