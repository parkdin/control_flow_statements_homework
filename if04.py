def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    pos_num = 0
    if a > 0:
        pos_num += 1
    if b > 0:
        pos_num += 1
    if c > 0:
        pos_num += 1
    return pos_num

print(main(-4, -4,6))