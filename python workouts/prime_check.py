num = int(input("enter the number:"))

# define a flag variable to check if the number has any divisors
flag = False

# Check if the number is 0 or 1
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # Check for factors from 2 to num-1
    for i in range(2, num):
        if (num % i) == 0:  # If there's a divisor other than 1 and num itself
            flag = True  # Mark the number as not prime
            break  # Exit the loop once a divisor is found

    # Check the flag to determine primality
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
