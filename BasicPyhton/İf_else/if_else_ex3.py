#Which year do you want to check?
year = int(input("Enter a year: "))

if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d is a leap year." % year)
else:
    print("%d is not a leap year." % year)

if  year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else: 
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year")  
else:
    print(f"{year} is not a leap year.")      
