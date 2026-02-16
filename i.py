year = int(input("Enter a year: ")) 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True 
else:
    leap_year = False
if leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")