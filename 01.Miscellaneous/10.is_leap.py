def is_leap(year):
    leap = False
    if year % 4 == 0:
        print("is leap")
    elif year % 100 == 0:
        print("No is leap")
    elif year % 100 == 0 and year % 400 == 0:
        print("is leap")  
    else: 
        print("No is leap")
year = int(input("enter year: "))
is_leap(year)
