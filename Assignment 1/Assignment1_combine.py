def lower_triangular_pattern(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n+1):
        print("* " * i)
    print()
    
def upper_triangular_pattern(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()
    
def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()  

n1 = int(input("Enter the number of rows lower triangle : "))
lower_triangular_pattern(n1)

n2 = int(input("Enter the number of rows for upper triangle : "))
upper_triangular_pattern(n2)

n3 = int(input("Enter the number of rows for pyramid : "))
pyramid(n3)
