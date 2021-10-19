# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    
    n = len(string)
    print(n)
    substring = [[x for x in range(k)]for x in range(n//k)]
    print(substring)
    # initialize substring[n/k][k] that would be a two dimensional list
    # initialize buffer type list of size(k)
    test = {1, 3, 5, 1, 5, 1}
    print(test)

if __name__ == '__main__':
    merge_the_tools("AABCAAADA", 3)