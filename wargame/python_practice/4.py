#Given a number, it list all the divisor of that number

num = int(input("Insert a number: "))
x = range(2, num + 1)

for i in x:
    if ((num % i) == 0):
        print(i)
