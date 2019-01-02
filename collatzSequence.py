# The Collatz Sequence
# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(num):
    while num > 1:
        if num % 2 == 0:
            num = num / 2

        else:
            num = 3 * num + 1

        print(num)



print("Enter a number:")

inputNum = int(input())
collatz(inputNum)       


