def digital_root(n):
    if n < 10:
        return n
    x = 0
    for digit in str(n):
        x += int(digit)
    return digital_root(x)