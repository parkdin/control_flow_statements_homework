def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    result = 0
    two_digit = a > 9 and a < 100
    three_digit = a > 99 and a <1000
    even_num = a % 2
    if two_digit and even_num != 0:
        result = "Two-digit odd number"
    if two_digit and even_num == 0:
        result = "Two-digit even number"
    if three_digit and even_num != 0:
        result = "Three-digit odd number"
    if three_digit and even_num == 0:
        result = "Three-digit even number"
    return result

print(main(44))