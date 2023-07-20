from coffee import MENU,resources
# TODO: ask user what he wants to take

#Displays report
water=resources["water"]
milk=resources["milk"]
coffee=resources["coffee"]
money=0
def my_resources(water,milk,coffee,money):
    return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\n"


#TODO: check if ressources are sufficient

def check_resources(a):
    if a=="espresso":
        if water>=50 and coffee>=18:
            return True
        elif water>=50 and coffee<18:
            print("Sorry there not enough coffee")
        elif water<50 and coffee>=18:
            print("Sorry there is  not enough water")
        else:
            print("Sorry there is not enough water and coffee")
    elif a=="latte":
        if water>=200 and coffee>=24 and milk>=150:
            return True
        elif water<200 and coffee>=24 and milk>=150:
            print("there is not enough water")
        elif water>=200 and coffee<24 and milk>=150:
            print("there is not enough coffee")
        elif water>=200 and coffee>=24 and milk<150:
            print("there is not enough milk")
        else:
            print("there is not enough water, milk and coffee")
    elif a=="cappuccino":
        if water>=250 and coffee>=100 and milk>=24:
            return True
        elif water<250 and coffee>=100 and milk>=24:
            print("there is not enough water")
        elif water>=250 and coffee<100 and milk>=24:
            print("there is not enough coffee")
        elif water>=250 and coffee>=100 and milk<24:
            print("there is not enough milk")
        else:
            print("there is not enough water, milk and coffee")
continue_working=True
while continue_working:
    user_choice = input("What would you like? (espresso/ latte/ cappuccino) or type report to get the remaining ingredients: ").lower()

    #TODO: turn off the machine when user input off
    if user_choice=="off":
        continue_working=False
        print("Coffee machine is off")
    if user_choice=="report":
        print(my_resources(water,milk,coffee,money))
    choice=check_resources(user_choice)

    if choice:
        print("Please insert coins")
        quarters=float(input("How many quarters: "))
        dimes=float(input("How many dimes: "))
        nickles=float(input("How many nickles: "))
        pennies=float(input("How many pennies: "))
        value=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
        if user_choice=="espresso":
            if value>=1.5:
                water-=50
                coffee-=18
                money+=1.5
                change=(value-1.5)
                print(f"Here is {change} dollars in change")
                print(f"Here is your {user_choice}. Enjoy! ")
            else:
                print("Sorry that is not enough money, Money refunded")
        elif user_choice=="latte":
            if value>=2.5:
                water-=200
                milk-=150
                coffee-=24
                money += 2.5
                change=(value-2.5)
                print(f"Here is {change} dollars in change")
                print(f"Here is your {user_choice}. Enjoy! ")
            else:
                print("Sorry that is not enough money, Money refunded")
        elif user_choice=="cappuccino":
            if value>=3.0:
                change=(value-3.0)
                water -= 250
                milk -= 100
                coffee -= 24
                money += 3.0
                print(f"Here is {change} dollars in change")
                print(f"Here is your {user_choice}. Enjoy! ")
            else:
                print("Sorry that is not enough money, Money refunded")


