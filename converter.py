# Convert miles to kilometers
def milesTokm(miles):
    km = miles * 1.60934
    print(miles, "miles is", km, "kilometers")
# Convert Fahrenheit to Celsius
def FahToCel(Fah):
    Cel = (Fah - 32) * 5.0/9.0
    print(Fah, "Fahrenheit is", Cel, "Celsius")
# Convert gallons to liters
def GalToLit(Gal):
    Lit = Gal * 3.785
    print(Gal, "gallon is", Lit, "Litter")
# Convert pounds to Kilogram
def PoundsToKg(pounds):
    kg = pounds * 0.45359
    print(pounds, "pounds is", kg, "kilogram")
# Convert Inches to cm
def InchesToCm(inches):
    cm = inches * 2.54
    print(inches, "inches is", cm, "centemeter")
# Ask user for units to be converted
def main():
    miles = float(input("Enter miles: "))
    milesTokm(miles)
    Fah = float(input("Enter Fahrenheit: "))
    FahToCel(Fah)
    Gal = float(input("Enter gallons: "))
    GalToLit(Gal)
    pounds = float(input("Enter pounds: "))
    PoundsToKg(pounds)
    inches = float(input("Enter inches: "))
    InchesToCm(inches)
main()


    