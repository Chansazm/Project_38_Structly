def anagrams(s1,s2):
    return countitems(s1) == countitems(s2)


def countitems(s):
    map = {}
    for char in s:
        if char not in map:
            map[char] = 1
        else: 
            map[char] += 1
    return map
            



#catss {c:1,a:1,t:1,s:2}
print(countitems('catss'))