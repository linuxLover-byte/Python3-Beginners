# Which year do you want to check?
year = int(input("Enter a year --->   "))



divisionBy4 = year % 4
divisionBy100 = year % 100
divisionBy400 = year % 400



if divisionBy4 == 0:
    if divisionBy100 == 0:
        if divisionBy400 == 0:
            print('Leap year')
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print('Not a leap year')
