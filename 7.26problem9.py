def print_triangular_numbers(n):
    if not isinstance(n, int) or n <= 0:
        print("Error: n must be a positive integer.")
        return
    for i in range(1, n + 1):
        triangular_num = i * (i + 1) // 2
        print(i, triangular_num)


print_triangular_numbers(5)
