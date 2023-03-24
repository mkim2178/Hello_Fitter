
"""
GolfClubs_and_Storages.py includes GolfClub, ClubFitter, and Storage objects!
"""


from Customer_ClubFitter_Exceptions_GolfClub_Storage.ClubFitter import ClubFitter
from Customer_ClubFitter_Exceptions_GolfClub_Storage.GolfClub import GolfClub
from Customer_ClubFitter_Exceptions_GolfClub_Storage.Storage import Storage

# GolfClub and ClubFitter objects can be added infinitely!

# GolfClub objects -------------------------------------------

# Titleist

Titleist_Driver1 = GolfClub("Titleist", "Driver", "TSR3", "R", 9.0, "Kuro Kage", "Golf Pride")
Titleist_Driver2 = GolfClub("Titleist", "Driver", "TSR2", "L", 10.0, "Diamana", "Golf Pride")

Titleist_Fairway1 = GolfClub("Titleist", "Fairway", "TSI1", "L", 15.0, "Tour AD", "Golf Pride")
Titleist_Fairway2 = GolfClub("Titleist", "Fairway", "TSR2+", "R", 13.0, "HZRDUS", "Golf Pride")

Titleist_Hybrid1 = GolfClub("Titleist", "Hybrid", "TSI3", "R", 20.0, "Tensei", "Golf Pride")
Titleist_Hybrid2 = GolfClub("Titleist", "Hybrid", "TSI2", "R", 21.0, "HZRDUS", "Golf Pride")


# TaylorMade

TaylorMade_Driver1 = GolfClub("TaylorMade", "Driver", "Stealth Plus", "R", 9.0, "Kai\'li", "Lamkin")
TaylorMade_Driver2 = GolfClub("TaylorMade", "Driver", "SIM2 Max", "L", 10.5, "Fujikura", "Golf Pride")

TaylorMade_Fairway1 = GolfClub("TaylorMade", "Fairway", "Stealth", "R", 15.0, "Fujikura", "Lamkin")
TaylorMade_Fairway2 = GolfClub("TaylorMade", "Fairway", "M4", "L", 18.0, "Fujikura", "Golf Pride")

TaylorMade_Hybrid1 = GolfClub("TaylorMade", "Hybrid", "Stealth Plus Rescue", "R", 19.5, "HZRDUS", "Lamkin")
TaylorMade_Hybrid2 = GolfClub("TaylorMade", "Hybrid", "Stealth UDI", "L", 23.0, "Aldila", "Super Stroke")


# Callaway

Callaway_Driver1 = GolfClub("Callaway", "Driver", "Rogue ST Max", "R", 9.0, "Tensei", "Golf Pride")
Callaway_Driver2 = GolfClub("Callaway", "Driver", "Great Big Bertha", "L", 10.5, "UST Mamiya", "Winn")


Callaway_Fairway1 = GolfClub("Callaway", "Fairway", "Rogue ST LS", "R", 13.5, "Tensei", "Golf Pride")
Callaway_Fairway2 = GolfClub("Callaway", "Fairway", "Great Big Bertha", "L", 18.0, "UST Mamiya", "Winn")


Callaway_Hybrid1 = GolfClub("Callaway", "Hybrid", "Rogue ST Pro", "R", 20.0, "Tensei", "Golf Pride")
Callaway_Hybrid2 = GolfClub("Callaway", "Hybrid", "Apex 21", "L", 24.0, "UST Mamiya", "Super Stroke")


# 'every_golf_club' is a list that includes every GolfClub object.
every_golf_club = [Titleist_Driver1, Titleist_Driver2, Titleist_Fairway1, Titleist_Fairway2, Titleist_Hybrid1, Titleist_Hybrid2,
                   TaylorMade_Driver1, TaylorMade_Driver2, TaylorMade_Fairway1, TaylorMade_Fairway2, TaylorMade_Hybrid1, TaylorMade_Hybrid2,
                   Callaway_Driver1, Callaway_Driver2, Callaway_Fairway1, Callaway_Fairway2, Callaway_Hybrid1, Callaway_Hybrid2
                   ]

# GolfClub objects ----------------------------------------------





# ClubFitter objects ------------------------

fitter1 = ClubFitter('Aaron', 1, 100)
fitter2 = ClubFitter('Bradley', 2, 200)
fitter3 = ClubFitter('Chris', 3, 300)
fitter4 = ClubFitter('Donna', 4, 400)
fitter5 = ClubFitter('Eric', 5, 500)
fitter6 = ClubFitter('Frank', 6, 600)
fitter7 = ClubFitter('Georgia', 7, 700)
fitter8 = ClubFitter('Henry', 8, 800)
fitter9 = ClubFitter('Issac', 9, 900)
fitter10 = ClubFitter('Jim', 10, 1000)

# 'every_fitter' is a list that includes every ClubFitter object.
every_fitter = [fitter1, fitter2, fitter3, fitter4, fitter5,
                fitter6, fitter7, fitter8, fitter9, fitter10]

# ClubFitter objects --------------------------





# Storage objects-------------------------------
# The program only requires two different Storage objects for new shafts and grips.

shaft_storage = Storage("Shaft Storage", {"Fujikura": 5, "Diamana": 3, "Tour AD": 9, "UST Mamiya": 10, "Kuro Kage": 1, "Tensei": 10, "HZRDUS": 6, "Aldila": 12, "Kai\'li": 15, "KBS": 20})
grip_storage = Storage("Grip Storage", {"Golf Pride": 20, "Lamkin": 5, "Super Stroke": 9, "Winn": 11, "Iomic": 3})

# Storage objects-------------------------------

