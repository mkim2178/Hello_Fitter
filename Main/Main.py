
"""
This is the place where Hello_Fitter service starts!
Various functions are located to limit inputs and help the customer to fit their golf clubs.
"""

from Customer_ClubFitter_Exceptions_GolfClub_Storage.ClubFitter import *
from Customer_ClubFitter_Exceptions_GolfClub_Storage.Customer import *
from Customer_ClubFitter_Exceptions_GolfClub_Storage.EveryException import *
from GolfClubs_Storages import *


def only_numbers(maximum):
    """
    This function will return an integer that customer selected from a certain selection.
    It will only return an integer number when these requirements if...

    * Input should be only integer (float, str, or any other type of variable is not allowed)
    * If input is integer but greater than maximum or less than 1, it will throw an 'InvalidNumberInput' customized exception.

    :param int maximum: a maximum number of integer.
    :return: an integer that customer typed in.
    """


    while True:

        try:

            n = int(input("-> "))

            if n < 1 or n > maximum:
                raise InvalidNumberInput

            return n

        except ValueError:
            print(f"Invalid Input! Please input an integer.")
        except InvalidNumberInput:
            print(f"Invalid Input! Input should be between 1 to {maximum}.")


def input_name():
    """
    This function will return a customer's name.
    It will let customer type his/her name.
    It will only allow alphabets.

    'isalpha()' built-in function only returns True if a string only includes alphabets.

    :return: a string (customer's name) that customer typed in.
    """


    print("What is your name?")

    while True:

        try:

            name = input("-> ")

            if not name.isalpha():
                raise InvalidNameInput

            return name

        except InvalidNameInput:
            print("Invalid Input! Your name should only include alphabets.")


def select_golf_clubs():
    """
    This function will return a list of customer's golf clubs.

    Here is the logic...

    1. It will first ask the number of golf clubs that customer want to get a club fitting.
    WHILE LOOP STARTS------
    2. Then it will print out the list of customer's golf clubs and let the customer select a number that corresponds a certain golf club.
    3.
    FOR LOOP STARTS------
        First, it will print out every golf club from 'every_golf_club' list.
        Next, it will call the only_numbers function with current length of 'every_golf_club' list as an argument.
        Then, it will subtract 1 because the list of golf club starts from 1 to current length of 'every_golf_club' list, but our list index starts from 0
        Finally, it will return the 'select' integer
    FOR LOOP ENDS------

    4. The selected golf club will be added into a list.
    WHILE LOOP ENDS------
    5. Finally, the list of golf clubs that customer selected will be returned.

    :return: a list of 'GolfClub' objects that customer selected.
    """


    lst_of_golf_clubs = []

    print()
    print(f"How many golf clubs do you want to fit? (You have {len(every_golf_club)} golf clubs).")  # the length of 'every_golf_club' list can be changed by adding more GolfClub objects into the 'every_golf_club' list.

    amount = only_numbers(len(every_golf_club))


    while amount > 0:

        for i in range(len(every_golf_club)):
            print(f"{i + 1}. {every_golf_club[i]}")

        select = only_numbers(len(every_golf_club)) - 1  # should subtract 1 because the program shows the menu with numbers 1 to x but list index starts from 0.

        lst_of_golf_clubs.append(every_golf_club[select])
        every_golf_club.pop(select)
        amount -= 1

    return lst_of_golf_clubs


def input_balance():
    """
    This function will return customer's starting balance.
    It will let customer input his/her starting money (integer or float).
    It will only allow customer to input integer or float number; otherwise, it will throw an 'ValueError.'
    The customer should possess at least $1000.0 from his/her first service so if he/she input less than 1000.0,
    it will throw an 'InvalidNumberInput' customized exception.

    :return: a float that represents customer's starting money.
    """

    print()
    print("How much money do you want to start?")

    while True:

        try:

            amount = float(input("-> "))

            if amount < 1000:
                raise InvalidNumberInput

            return amount

        except ValueError:
            print("Invalid Input! You should only input numbers (integer or float).")

        except InvalidNumberInput:
            print("Invalid Input! Your should add at least $1000 (amount of $ >= 1000).")


def select_main_menu():
    """
    This function visualize the main menu of Hello_Fitter program.
    It will show 6 different actions to the customer and let customer choose one of these actions.
    Every exception will be handled by calling 'only_numbers' function (the 'maximum' argument should be 6 because there are 6 different actions).

    :return: an integer that customer selected from the main menu.
    """

    print()
    print("1. Fit Shaft OR Grip | 2. Fit Loft | 3. Add Money | 4. My Selected Golf Clubs | 5. My Info | 6. Quit")

    menu = only_numbers(6)  # we only have 1, 2, 3, 4, 5, or 6 on main menu so the maximum value for menu input will be 6.

    return menu


def select_mini_menu():
    """
    This function visualize a mini menu that represents customer's next action.
    Customer will choose 1 if he/she wants to change his/her golf club's shaft; otherwise, it he/she wants to change his/her golf club's grip.
    Every exception will be handled by calling 'only_numbers' function (the 'maximum' argument should be 2 because there are 2 different actions).

    :return: an integer that customer selected from the mini menu.
    """

    print()
    print("1. Shaft | 2. Grip")

    menu = only_numbers(2)

    return menu


def select_one_golf_club(golf_clubs):
    """
    This function will visualize the 'golf_clubs' list that customer selected from 'every_golf_club' list.
    It will return an integer (the index of the list) that customer selected from 'golf_clubs' list.
    Every exception will be handled by calling 'only_numbers' function, and it will be decremented by 1.
    Because the visualized menu's number starts from 1 to length of 'golf_clubs' list.
    However, the index of list starts from 0, so it will subtract 1 from selected integer.

    :param list golf_clubs: a list that customer selected from 'every_golf_club' list.
    :return: an integer that corresponds the index of selected 'GolfClub' object from 'golf_clubs' list (this is contained inside 'Customer' object).
    """

    print()
    print("Select one golf club.")

    for i in range(len(golf_clubs)):

        print(f"{i + 1}. {golf_clubs[i]}")

    select = only_numbers(len(golf_clubs)) - 1

    return select


def select_new_item(current):
    """
    This function will return a new item from 'current' (this will be 'shaft_storage' or 'grip_storage') storage.
    The customer will type the name of the shaft/grip that want to be replaced to his/her selected golf club.

    Here is the logic...

    1. First, the customer should type the name of the new item (string input). It will obviously visualize remaining shafts/grips by using 'current' parameter that customer previously selected.
    2. If customer input is valid, the 'current' ('Storage' object) will call 'take_item' method to decrement 1 from the 'storage' dictionary (class attribute of 'current' object)
    3. Finally, it will return the name of the new item (string).

    *** IMPORTANT ***
    The customer should check the spelling, uppercase, and space of the input string (it will throw an InvalidNameInput exception if the input is invalid).
    The 'current' ('Storage' object) will check 'storage' dictionary (class attribute of 'current' ('Storage' object) object).

    :param obj current: a 'Storage' object that will be used to check if new item exists in selected 'Storage' object (will check the 'storage' dictionary that is located in certain 'Storage' object).
    :return: a string; the name of the new item.
    """

    print()
    print("Type the name of the new item.")


    for item in current.storage.items():

        print(f"Name: {item[0]} / Stock: {item[1]}")


    while True:

        try:

            new_item = input("-> ")

            if new_item not in current.storage or current.storage[new_item] == 0:
                raise InvalidNameInput

            current.take_item(new_item)  # decrement 1 from the storage dictionary (self.storage)

            return new_item

        except InvalidNameInput:
            print("Invalid Input! Your input is invalid by one of these reasons.")
            print("1. Your input should not include numbers or symbols.")
            print("2. You should check your spelling (careful with UPPER CASE letters and space).")
            print("3. Out of Stock!")


def input_more_money():
    """
    This function helps customer to add additional money into his/her balance.
    It will let customer input the amount of money (integer or float) that will be added into his/her current balance.
    It will raise 'InvalidNumberInput' customized exception if customer input is less than 1.
    It will raise 'ValueError' exception if customer input is not an integer or float number.

    :return: an integer or float that will be added to customer's balance.
    """

    print()
    print("How much money do you want to add?")

    while True:

        try:

            amount = float(input("-> "))

            if amount <= 0:
                raise InvalidNumberInput

            return amount

        except ValueError:
            print(f"Invalid Input! You should only input numbers (integer or float).")
        except InvalidNumberInput:
            print(f"Invalid Input! You should input positive numbers (amount of $ > 0).")


def at_least_thousand(customer):
    """
    This function will be called if customer's current balance is less than 1000.
    It visualizes two selection to customer.
    It returns an integer that customer selected (will be 1 or 2).

    :param obj customer: a 'Customer' object to print out customer's current balance.
    :return: an integer that customer selected.
    """

    print()
    print(f"Your current balance is {customer.balance}. You should own at least $1000.")
    print(f"1. Add Money | 2. Quit")

    select = only_numbers(2)

    return select


def select_fitter(customer, current_golf_club):
    """
    This function helps customer to select a club fitter.
    The parameters are 'Customer' object and 'GolfClub' object.  # ignore 'customer' parameter.

    Here is the logic...

    1. First, this function will print out the list of fitters by using 'every_fitter' list.
    2. Then, subtract 1 from customer's selection (as I explained before, the number of list will start from 1 but list index starts from 0).
    3. Next, this function will call the 'ability_validation' function to check if selected club fitter has enough ability to work on customer's selected golf club.
    3. Finally, if the customer made a valid input, it will return a 'ClubFitter' object that customer selected.

    :param obj customer: ignore this parameter
    :param obj current_golf_club: a 'GolfClub' object that customer selected.
    :return: a 'ClubFitter' object that customer selected.
    """

    print()
    print("Select one club fitter.")

    for i in range(len(every_fitter)):

        print(f"{i + 1}. {every_fitter[i]}")


    while True:

        try:

            select = only_numbers(len(every_fitter)) - 1

            if not ability_validation(every_fitter[select], current_golf_club):

                raise InvalidClubFitter

            return every_fitter[select]  # ClubFitter object

        except InvalidClubFitter:
            print(f"Invalid Input! This club fitter need more ability.")


def select_coupon_usage():
    """
    This function asks customer about the coupon usage.
    If customer input 1 (if customer want to use his/her coupon), the function will return True; otherwise, if customer does not want to use a coupon, it will return False.

    :return: a boolean value (customer want to use a coupon -> True, otherwise -> False).
    """

    print()
    print("Do you want to use your coupon?")
    print("1. Yes | 2. No")


    select = only_numbers(2)

    if select == 1:
        return True
    else:
        return False


def input_angle_amount():
    """
    This function will be called if the customer want to change his/her selected golf club's loft angle.
    If customer type a valid input, it will return a float value (amount of angle that will be added into his/her golf club).

    * If customer input is not an integer or float type value, it will throw a 'ValueError' exception.
    * If customer input is an integer or float but out of range between -1.0 and 1.0, it will throw a customized 'InvalidNumberInput' exception.

    :return: a float number (amount of angle that will be addedinto his/her selected golf club's loft angle).
    """

    print()
    print("How many degrees?")

    while True:

        try:

            amount = float(input("-> "))

            if amount > 1.0 or amount < -1.0:
                raise InvalidNumberInput

            return amount

        except ValueError:
            print("Invalid Input! You should only input numbers (integer or float).")
        except InvalidNumberInput:
            print("Invalid Input! The amount of degree should be between -1.0 to 1.0 degree.")


def start_hello_fitter():
    """
    This function is the most important function in 'Hello_Fitter' program.
    This is the place where the 'Hello_Fitter' program starts and ends.

    Here is the logic...

    1. The customer can input his/her name.
    2. The customer can add his/her golf clubs from 'every_golf_club' list (these golf clubs will be customized).
    3. The customer can add his/her starting money that will be used to get the service.
    4. The 'Customer' object will be created.
    5. The program will give a Welcome message and print out customer's information.
    WHILE LOOP STARTS -----
    6. The program will ask customer about his/her action (visualize the main menu).

        * option1 - 1. customer will select one golf club from his/her golf clubs
                    2. 'is_shaft' variable will be initialized as True (this will be changed if customer wants to change his/her golf club's grip).
                    3. customer will select one option from mini menu (shaft or grip?).

                    * mini-menu: select 1 - new item will be selected from 'Shaft_Storage.'
                                 select 2 - new item will be selected from 'Grip_Storage' and re-initialize 'is_shaft' variable into False.

                    4. customer will select one club fitter.
                    5. club fitter's 'golf_club' class attribute will be defined as 'golf_club' variable (this is a 'GolfClub' object that customer selected).
                    6. customer will make his/her decision about coupon usage.
                    7. call 'option_1' to customize customer's selected golf club.

        * option2 - same logic as option_1 but customer will input the amount of loft angle to change his/her selected golf club's loft angle.
                  - 'option_2' will be called instead of 'option_1' because the customer wants to customize the loft angle.

        * option3 - 1. customer will input a certain amount of money to add his/her current balance.
                    2. 'option_3' will be called.

        * option4 - call 'option_4' to print out every golf club that customer selected.

        * option5 - call 'option_5' to print out customer's information.

        * option6 - end the main while loop.
        WHILE LOOP ENDS (FIRST CASE) -----

    7. Inner while loop will start if customer wants to get additional service but his/her current balance is less than 1000.
       INNER WHILE LOOP STARTS -----
       * 'at_least_thousand' function will be called: select 1 - customer can add additional money
                                                      select 2 - inner while loop will and main while loop will end.
       INNER WHILE LOOP ENDS -----
    WHILE LOOP ENDS (SECOND CASE) -----

    :return: None.
    """


    name = input_name()
    golf_clubs = select_golf_clubs()
    balance = input_balance()
    customer = Customer(name, golf_clubs, balance)


    print()
    print(f"Welcome {customer.name}!")
    print(f"INFO: {customer}")

    run = True

    while run:

        option = select_main_menu()

        if option == 1:

            golf_club = customer.golf_clubs[select_one_golf_club(customer.golf_clubs)]
            is_shaft = True
            select = select_mini_menu()

            if select == 1:

                new_item = select_new_item(shaft_storage)


            else:

                new_item = select_new_item(grip_storage)
                is_shaft = False

            club_fitter = select_fitter(customer, golf_club)
            club_fitter.define_golf_club(golf_club)
            coupon = select_coupon_usage()

            customer.option_1(club_fitter, new_item, is_shaft, coupon)

            print()
            print("Fitted!")

        elif option == 2:

            golf_club = customer.golf_clubs[select_one_golf_club(customer.golf_clubs)]
            amount = input_angle_amount()
            club_fitter = select_fitter(customer, golf_club)
            club_fitter.define_golf_club(golf_club)
            coupon = select_coupon_usage()

            customer.option_2(club_fitter, amount, coupon)

            print()
            print("Fitted!")

        elif option == 3:

            customer.option_3(input_more_money())

        elif option == 4:

            customer.option_4()

        elif option == 5:

            print(customer)

        else:
            run = False

        while customer.balance < 1000.0:

            select = at_least_thousand(customer)

            if select == 1:
                customer.option_3(input_more_money())
            else:
                run = False
                break


    print()
    print("Good Bye!")


def main():
    """
    This is a main function.
    The 'start_Hello_fitter' function will be called and it wil start the program.
    """

    start_hello_fitter()


if __name__ == '__main__':
    main()

