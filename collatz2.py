# Karolina Szafran-Belzowska, 28/09/2019
# Collatz operation

n = int(input("Enter a positive integer: "))

# Keep looking until we reach 1.
# This assumes The Collatz conjecture is TRUE

while n != 1:
    # Print the current value of n
    print(n)

    # Check if n is even

    if n % 2 == 0:

    # If n is even, divide it by two

        n = n //2

    # If n is odd , multiply by 3 and +1
    
    else:
        n = (3*n)+1

print(n)
