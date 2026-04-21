def isPalindrome(x):
    x = str(x)
    pal = x[::-1]
    return pal == x

    # return str(x) == str(x)[::-1]