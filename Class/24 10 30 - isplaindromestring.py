def isPalindromeRecursion(s):
    '''if not(s): #s empty string
        return True
    elif len(s) == 1:
        return True'''
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindromeRecursion(s[1:len(s) - 1])
    
def isPalindromeInterative(s):
    L = len(s)
    result - True
    for i in range(int(L/2)):
        print(s[i], s[L-i], s[i] == s[L-i], "also", s[-(i+1)])
        '''s[i] == s[L-i]
        s[i] == s[-(i+1)]'''
        result = result and s[i] == s[L-i]
    return result

def isPalindromeWhile(s):
    L = len(s)
    result = True
    left = 0
    right = L-1
    while left < right:
        result = result and s[right] == s[left]
        left = left + 1
        right = right - 1
    return result



s = input("Write something: ")
print("Recursion: ", s, isPalindromeRecursion(s))
print("interactive: ", s, isPalindromeRecursion(s))
print("While: ", s, isPalindromeWhile(s))

    
