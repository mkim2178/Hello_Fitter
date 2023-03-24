
"""
A bunch of customized Exception classes. Details are explained inside each class!
"""


class InvalidCouponInput(Exception):
    """
    Raise if coupon input is not in self.coupons_amount list (input should be one of these three numbers: 5, 10, or 25)
    """
    pass


class InvalidNumberInput(Exception):
    """
    Raise if amount of golf club is 0 or over the length of every_golf_club list.
    OR
    Raise if amount of money is less than or equal to 0.
    """
    pass


class InvalidNameInput(Exception):
    """
    Raise if name includes any numbers or symbols which are not alphabets.
    """
    pass


class InvalidClubFitter(Exception):
    """
    Raise if selected club fitter's ability does not valid for the selected golf club that wanted to be fitted.
    """
    pass

