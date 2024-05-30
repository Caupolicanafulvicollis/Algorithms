def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        print("is leap")
    elif year % 100 == 0:
        leap = False
        print("No is leap")
    elif year % 100 == 0 and year % 400 == 0:
        leap = True
        print("is leap")  

year = int(input("enter year: "))
is_leap(year)