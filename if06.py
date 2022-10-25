def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    positive_num = 0
    if a > 0:
        positive_num += 1
    if b > 0:
        positive_num += 1
    if c > 0:
        positive_num += 1

    if positive_num > 1:
        positive_num = "there are a lot of positive numbers"
    else:
        positive_num = "there are a lot of negative numbers"
    return positive_num


