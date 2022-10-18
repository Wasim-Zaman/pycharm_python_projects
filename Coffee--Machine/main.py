from data import resources

money = 0
# TODO-1: Prompt the user by asking what whould you like? (expresso/latte/cappuccino):
on = True
while on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
# TODO-2: Turn off the coffee machine by entering 'off' to the prompt
    # use a secret key off for the switching off your coffee machine
    if choice == 'off'.lower():
        on = False
# TODO-3: Print report
    elif choice == 'report'.lower():
        for key in resources:
            print(f'{key}: {resources[key]}')
        print(f'Money: {money}')
# TODO-4 Check resources sufficient?😊😍
# TODO-5 Process the coin
