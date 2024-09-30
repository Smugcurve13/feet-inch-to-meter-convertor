#function to convert feet and inch to meters

def convert(feet,inch):
    feet = float(feet)
    inch = float(inch)

    meters = feet * 0.3048 + inch * 0.025
    return meters