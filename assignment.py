def product_of_numbers(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


def check_prime_division(n):
    prime_checks = {}
    for i in range(2, n+1):
        prime_checks[i] = all(i % j != 0 for j in range(2, i))
    return prime_checks

# Example usage:
print(check_prime_division(10))
# Output: {2: True, 3: True, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False, 10: False}