
"""
The ClubFitter class represents the club fitter. He/She can change the shaft, grip, or loft of the golf club!
"""


class ClubFitter:

    def __init__(self, name, ability, cost):
        """
        This is an init method (constructor that initializes the ClubFitter object).
        It includes the club fitter's name, ability, cost, and current golf club that he/she will work on.

        :param str name: club fitter's name.
        :param int ability: club fitter's ability (1 <= ability <= 10).
        :param float cost: the amount of money that customer should pay.
        """

        self.name = name
        self.ability = ability
        self.cost = cost
        self.golf_club = None  # the default value is None but will be initialized to 'GolfClub' object after a customer choose a golf club.


    def define_golf_club(self, current_golf_club):
        """
        This method initialize the 'golf_club' class attribute.
        The 'current_golf_club' parameter will be a 'GolfClub' object.

        :param obj current_golf_club: a golf club that club fitter will work on.
        :return: None.
        """

        self.golf_club = current_golf_club


    def fit_golf_club(self, new_item, is_shaft):
        """
        This method re-defines the current golf club's shaft (or grip) into new shaft (or grip).
        If the parameter 'is_shaft' is True, the club fitter will change the shaft.
        Otherwise, he/she will change the grip.

        :param str new_item: a new item that will replace current golf club's shaft (or grip).
        :param bool is_shaft: a boolean value that states the change of shaft (or grip).
        :return: None.
        """

        if is_shaft:
            self.golf_club.shaft = new_item
        else:
            self.golf_club.grip = new_item


    def fit_loft(self, amount):
        """
        This method redefines the current golf club's loft.
        The parameter 'amount' will be added into current golf club's loft.
        The parameter 'amount' has a limited range (-1.0 <= amount <= 1.0).

        :param float amount: the amount of loft angle that will be added on current golf club's loft.
        :return: None.
        """

        self.golf_club.loft += amount


    def __repr__(self):
        """
        This is a repr method; an object representation of the 'ClubFitter' object (the format is formal).

        :return: a string that represents the 'ClubFitter' object (ex: ClubFitter(Minwoo, 8, 800)).
        """

        return f"ClubFitter({self.name}, {self.ability}, {self.cost})"


    def __str__(self):
        """
        This is a str method; also an object representation of the 'ClubFitter' object, but it is legible for human (informal).
        It includes repr() built-in function to include the quotes.

        If you only put self.name, it will give >>> Minwoo
        However, if you put repr(self.name), this will give >>> 'Minwoo'

        :return: a string that represents the 'ClubFitter' object (ex: "Name: 'Minwoo' / Ability: 8 / Cost: 800")
        """

        return f"Name: {repr(self.name)} / Ability: {self.ability} / Cost: {self.cost}"





def ability_validation(club_fitter, current_golf_club):
    """
    This function checks the club fitter's validation.
    If current club fitter's ability is between 1 ~ 3, he/she can only work on 'Driver.'
    If current club fitter's ability is between 4 ~ 7, he/she can only work on 'Driver' and 'Fairway.'
    If current club fitter's ability is between 8 ~ 10, he/she can work on every type of golf club.

    * You can just look at the ClubFitter Table.png to see the table chart.

    :param obj club_fitter: a 'ClubFitter' object that customer selected.
    :param obj current_golf_club: a 'GolfClub' object that will be fitted.
    :return: a boolean value.
    """

    if (current_golf_club.club_type == 'Driver' and 1 <= club_fitter.ability <= 10) or \
       (current_golf_club.club_type == 'Fairway' and 4 <= club_fitter.ability <= 10) or \
       (current_golf_club.club_type == 'Hybrid' and 8 <= club_fitter.ability <= 10):

        return True

    else:
        return False

