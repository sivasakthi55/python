years = [2027,2028,2029,2030]  # You have hardcoded a year, but you can also get user input with: year = int(input("Enter a year: "))

# Check if the year is divisible by 400 and also divisible by 100 (century year)
for year in years:

        if (year % 400 == 0) and (year % 100 == 0):
            print("{0} is a leap year".format(year))  # It's a leap year

        # If it's not divisible by 100 but divisible by 4, it's a leap year
        elif (year % 4 == 0) and (year % 100 != 0):
            print("{0} is a leap year".format(year))  # It's a leap year

        # If none of the above conditions are met, it's not a leap year
        else:
            print("{0} is not a leap year".format(year))  # Not a leap year
