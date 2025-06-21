def lower_triangular_pattern(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n+1):
        print("* " * i)
    print()

n = int(input("Enter the number of rows (n): "))

lower_triangular_pattern(n)
