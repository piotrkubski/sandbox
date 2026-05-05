def needleInHaystack(haystack, needle):
    if needle in haystack:
        return haystack.find(needle)
    else: 
        return -1
    
    # n = len(haystack)
    # m = len(needle)

    # for i in range(n - m + 1):
    #     j = 0
    #     while j < m and haystack[i + j] == needle[j]:
    #         j += 1
        
    #     if j == m:
    #         return i 
        
    # return -1
