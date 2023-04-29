def isAnagram(str_a,str_b):
    if len(str_b) > len(str_a):
        return False
    str_a=str_a.lower()
    str_b=str_b.lower()
    dictb = dict()
    for c in str_b:
        if (c not in dictb):
            dictb[c] = 1
        else:
            dictb[c] += 1
    
    for i in range(0, len(str_a)-len(str_b)+1): # don't forget +1 here since the range does not touch the right-hand side value
        sub = str_a[i:i+len(str_b)]
        dict_sub = dict()
        for k in sub:
            if k not in dict_sub:
                dict_sub[k] = 1
            else:
                dict_sub[k] += 1
        if dict_sub == dictb:
            return True
    return False

def main():
    # str_a = "crowd"
    str_a = "Here come dots and lines that helped build America,"
    # str_b = "word"
    str_b = "The Morse Code"
    print(isAnagram(str_a,str_b))

if __name__ == "__main__":
    main()