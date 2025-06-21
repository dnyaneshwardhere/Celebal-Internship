
def upper_triangular_pattern(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()
    

n = int(input("Enter the number of rows (n): "))

upper_triangular_pattern(n)

