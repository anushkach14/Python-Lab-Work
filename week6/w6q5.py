def days_in_month(month):
    if month in (1,3,5,7,8,10,12):
        print("days=31")
    elif month in (4,6,9,11):
        print("days=30")
    elif month==2:
        print("Days=28 or 29(leap year)")
    else:
        print("Invalid input.")

month=int(input("Enter month number(1-12): "))
print(days_in_month(month))