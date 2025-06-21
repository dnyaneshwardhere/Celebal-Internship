
def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()  

n = int(input("Enter the number of rows (n): "))

pyramid(n)
