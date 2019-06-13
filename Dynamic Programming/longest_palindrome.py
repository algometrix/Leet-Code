import numpy


def longest_palindrome(s):
    max_length = 1
    result = ''
    length = len(s)

    if length == 0:
        return s

    if length == 1:
        return s
            
    if length == 2:
        if s[::-1] == s:
            return s
        else:
            s[0]

    A = []
    for i in range(0, length):
        A.append([0] * length)
        A[i][i] = 1

    for k in range(0, length):
        l = 0
        for p in range(k + 1, length):
            l += 1
            j = k + l + 1
            i = p - k
            #print('{} : {}'.format(i - 1, j - 1))
            if s[i-1] == s[j-1]:
                if (i < j - 2 or i == j-2) and A[i][j-2]!=0:
                    A[i-1][j-1] = A[i][j-2] + 2
                elif i > j - 2:
                    A[i-1][j-1] = A[i][j-2] + 2
                
                
                if A[i-1][j-1] > max_length:
                    result = s[i-1: j]
                    max_length = A[i-1][j-1]

    #print(numpy.matrix(A))
    if max_length == 1:
        return s[0]
    return result


if __name__ == "__main__":
    s = 'a'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'aa'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'aaa'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'aba'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'abb'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'aaab'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'racecar'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'racedcar'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))

    s = 'value'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))
    
    s = 'ninja'
    print('Longest Palindrome : {} for {}'.format(longest_palindrome(s), s))
