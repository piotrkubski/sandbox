def  longestCommonPrefix(strs):
    common = strs[0]
    for word in strs[1:]:
        i = 0
        while i < len(word) and i < len(common) and word[i] == common[i]:
            i += 1
        else:
            common = common[:1]
        return common
    
    # strs.sort()
    # s = '' 
    # i = 0
    # while i < len(strs[0]):
    #     if strs[0][i] == strs[len(strs) - 1][i]:
    #         s += strs[0][i]
    #     else:
    #         break
    #     i += 1
    # return s