
"""
The GolfClub class represents the golf club. It includes the detailed parts of a certain golf club!
"""


class GolfClub:

    def __init__(self, brand_name, club_type, model_name, hand, loft, shaft, grip):
        """
        This is an init method (constructor that initializes the GolfClub object).
        It contains the golf club's brand name, type, model name, hand, loft, shaft name, and grip name.

        :param str brand_name: golf club's brand name (ex: Titleist, TaylorMade, Callaway, etc.).
        :param str club_type: a type of golf club (Should be one of these three: Driver, Fairway, Hybrid).
        :param str model_name: a model name (ex: TSR3 (Titleist), Stealth (TaylorMade), Rogue (Callaway)).
        :param str hand: a letter that represents the right/left-handed golf club.
        :param float loft: a loft angle of golf club.
        :param str shaft: golf club's shaft name (shaft brand name).
        :param str grip: golf club's grip name (grip brand name).
        """

        self.brand_name = brand_name
        self.club_type = club_type
        self.model_name = model_name
        self.hand = hand
        self.loft = loft
        self.shaft = shaft
        self.grip = grip


    def __repr__(self):
        """
        This is a repr method; an object representation of the 'GolfClub' object (the format is formal).

        :return: a string that represents the 'GolfClub' object (ex: GolfClub(Titleist, Driver, TSR3, R, 9.0, HZRDUS, Golf Pride)).
        """

        return f"GolfClub({self.brand_name}, {self.club_type}, {self.model_name}, {self.hand}, {self.loft}, {self.shaft}, {self.grip})"


    def __str__(self):
        """
        This is a str method; also an object representation of the 'GolfClub' object, but it is legible for human (informal).
        It includes repr() built-in function to include the quotes.

        If you only put self.brand_name, it will give >>> Titleist
        However, if you put repr(self.brand_name), this will give >>> 'Titleist'

        :return: a string that represents the 'GolfClub' object (ex: "Brand: 'Titleist' / Type: 'Driver' / Model: 'TSR3' / Hand: 'R' / Loft: 9.0 / Shaft: 'HZRDUS' / Grip: 'Golf Pride'")
        """

        return f"Brand: {repr(self.brand_name)} / Type: {repr(self.club_type)} / Model: {repr(self.model_name)} / Hand: {repr(self.hand)} / Loft: {self.loft} / Shaft: {repr(self.shaft)} / Grip: {repr(self.grip)}"
