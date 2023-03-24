
"""
The Customer class represents customer!
* It includes customer's information.
* It imports customized exceptions from EveryException.py.
* It also import 'random' module to use 'choice' function to give a random number from these three numbers: 5, 10, 25 (will be explained from 'get_coupon' method).
"""

import random

from Customer_ClubFitter_Exceptions_GolfClub_Storage.EveryException import InvalidCouponInput



class Customer:

    def __init__(self, name, golf_clubs, balance):
        """
        This is an init method (constructor that initializes the Customer object).
        It includes the customer's name, selected golf clubs that will be customized, and balance (money).

        :param str name: customer's name.
        :param list golf_clubs: a list of GolfClub objects that customer selected.
        :param float balance: customer's balance (money that will be used: should be at least $1000).
        """

        self.name = name
        self.golf_clubs = golf_clubs
        self.balance = balance
        self.coupons = {5: 0, 10: 0, 25: 0}  # default
        self.amount_of_service = 0  # default
        self.coupons_amount = [5, 10, 25]





    def option_1(self, club_fitter, new_item, is_shaft, coupon):

        """
        This method will be called if customer wants to change shaft/ grip.
        If 'coupon' parameter is True, this means the customer wants to use his/her coupons.
        Otherwise, the customer does not want to use his/her coupons.

        Here is the detailed logic...

        1. First, check if customer wants to use his/her coupons.
        2. If coupon is true, check customer has coupons by using 'check_coupon' method.
        3. If 'check_coupon' method returns True, call 'show_coupon_menu' method to visualize customer's coupons.
        4. If 'check_coupon' method returns False or if 'coupon' is False, the program will give a message and take the money from customer's 'balance' (balance = balance - club fitter's cost).
        5. After customer's payment, it will call 'fit_golf_club' method with using 'club_fitter' object (club fitter that customer chose).
        6. Increment 'amount_of_service' by 1 to count the customer's service usage.
        7. Finally, call 'get_coupon' method to check if customer can receive a free coupon.

        :param obj club_fitter: a ClubFitter object that customer selected.
        :param str new_item: the name of new item.
        :param bool is_shaft: If 'is_shaft' is True, the customer wants to change shaft; otherwise, the customer wants to change grip.
        :param bool coupon: If 'coupon' is True, the customer wants to use a coupon; otherwise, the customer does not want to use the coupon.
        :return: None.
        """

        if coupon:

            if self.check_coupon():

                self.show_coupons(club_fitter)

            else:

                print()
                print("You don\'t have a coupon. No Discount.")

                self.balance -= club_fitter.cost

        else:

            self.balance -= club_fitter.cost

        club_fitter.fit_golf_club(new_item, is_shaft)

        self.amount_of_service += 1

        self.get_coupon()


    def option_2(self, club_fitter, amount, coupon):
        """
        This method will be called if customer wants to change the loft angle.
        The logic of 'option_2' method is same as the 'option_1' method.
        However, after the payment, the 'club_fitter' object will call 'fit_loft' method to change the loft angle.

        :param obj club_fitter: a ClubFitter object that customer selected.
        :param float amount: the amount of angle that customer want to change (this is limited between -1.0 to 1.0 degrees).
        :param bool coupon: If 'coupon' is True, the customer wants to use a coupon; otherwise, the customer does not want to use the coupon.
        :return: None.
        """

        if coupon:

            if self.check_coupon():

                self.show_coupons(club_fitter)


            else:

                print()
                print("You don\'t have a coupon. No Discount.")

                self.balance -= club_fitter.cost

        else:

            self.balance -= club_fitter.cost  # this will change if customer uses a coupon


        club_fitter.fit_loft(amount)

        self.amount_of_service += 1

        self.get_coupon()





    def option_3(self, amount):
        """
        This method will be called if customer wants to add additional amount of money.

        :param float amount: the amount of money that will be added to customer's balance.
        :return: None.
        """

        self.balance += amount


    def option_4(self):
        """
        This method will be called if customer wants to check his/her selected golf clubs that will be changed.

        :return: None.
        """

        print()
        print("*******SELECTED GOLF CLUBS**********")
        i = 1
        for club in self.golf_clubs:
            print(f"{i}. {club}")
            i += 1
        print("************************************")



    def check_coupon(self):
        """
        This method checks if customer has a coupon.
        A for loop will be used to navigate 'coupons' dictionary.
        'item[1]' represents the value and if 'item[1]' is greater than 0, it returns True (at least 1 coupon exists inside 'coupons' dictionary).

        :return: a boolean value (if customer has a coupon, it will return True; otherwise, return False).
        """

        for item in self.coupons.items():  # coupons.items() give a pair (key, value).

            if item[1] > 0:
                return True

        return False


    def show_coupons(self, club_fitter):
        """
        This method will visualize customer's 'coupons' dictionary.
        The customer can type one of these numbers: 5, 10, 25 (these are the name of the coupons (5%, 10%, and 25% coupon))

        Here is the logic:
        1. First, the customer will input the name of the coupons (5, 10, or 25).
        2. If he/she type a wrong name or if the amount of coupon is 0, the method will throw a customized exception (InvalidCouponInput)
           ex1: if the amount = 24 -> wrong name.
           ex2: if the amount = 25 but coupons[amount] = 0 -> the amount of 25% coupon is 0.
        3. If customer type a valid input, the method will call 'use_coupon' method.
        4. The while loop will be ended by the break statement.

        :param obj club_fitter: a 'ClubFitter' object that the customer has selected.
        :return: None.
        """

        print("Type the amount of coupon.")

        for item in self.coupons.items():
            print(f"{item[0]}% coupon / Amount: {item[1]}")

        while True:

            try:

                amount = int(input("-> "))

                if amount not in self.coupons_amount or self.coupons[amount] == 0:
                    raise InvalidCouponInput

                self.use_coupon(club_fitter, amount)
                break

            except InvalidCouponInput:
                print("Invalid Input! Your input is invalid by one of these reasons.")
                print("1. The input should be one of these numbers: 5, 10, 25.")
                print("2. You don\'t have that coupon.")
            except ValueError:
                print("Invalid Input! Please input an integer.")




    def use_coupon(self, club_fitter, amount):
        """
        This method will be called if the customer made a valid input from 'show_coupons' method.
        The 'amount'% coupon will be used so the value of 'coupons[amount]' should be decremented by 1.
        The 'balance' will also be decremented by the following formula -> balance = club fitter's cost - club fitter's cost * amount / 1000.

        :param obj club_fitter: a ClubFitter object that customer selected.
        :param int amount: the name of the coupon (will be one of these integers: 5, 10, and 25).
        :return: none.
        """

        print("Discount applied!")

        self.coupons[amount] -= 1  # 'amount'% coupon used

        self.balance -= club_fitter.cost - club_fitter.cost * amount / 100



    def get_coupon(self):
        """
        This method will be called the last part of 'option_1' and 'option_2' method.
        Customer will receive a random coupon on every fifth service.

        Here is the logic...

        1. If customer's 'amount_of_service' = 5, the 'choice' built-in function from 'random' module will give one number from 'coupons_amount' list (this will be the 'discount_amount' variable).
           * Otherwise, it will give a message: "You need x amount of service(s) to receive a coupon."
        2. Then, it will increment coupons[discount_amount] by 1 to count the coupon.
        3. Next, it will initialize the 'amount_of_service' to 0 because the customer can only receive coupon on every fifth service.
        4. Finally, it will give a message "You got an x% coupon."

        :return: None.
        """

        if self.amount_of_service == 5:

            discount_amount = random.choice(self.coupons_amount)

            self.coupons[discount_amount] += 1

            self.amount_of_service = 0

            print("***********************")
            print(f"*You got a {discount_amount}% coupon!*")
            print("***********************")

        else:
            print(f"You need {5 - self.amount_of_service} amount of service(s) to receive a coupon!")


    def __repr__(self):
        """
        This is a repr method; an object representation of the 'Customer' object (the format is formal).

        :return: a string that represents the 'Customer' object (ex: Customer(Minwoo, [GolfClub object1, GolfClub object2, ...], 1000.0, {5:0, 10:0, 25:0}, 0)).
        """

        return f"Customer({self.name}, {self.golf_clubs}, {self.balance}, {self.coupons}, {self.amount_of_service})"


    def __str__(self):
        """
        This is a str method; also an object representation of the 'Customer' object, but it is legible for human (informal).
        It includes repr() built-in function to include the quotes.

        If you only put self.name, it will give >>> Minwoo
        However, if you put repr(self.name), this will give >>> 'Minwoo'

        :return: a string that represents the 'Customer' object (ex: "Customer Name: 'Minwoo' / GolfClubs: [GolfClub object1, GolfClub object2...] / Balance: 1000.0 / Coupons: {5:0, 10:0, 25:0} / Amount of Service: 0")
        """

        return f"Customer Name: {repr(self.name)} / GolfClubs: {self.golf_clubs} / Balance: {self.balance} / Coupons: {self.coupons} / Amount of Service: {self.amount_of_service}"

