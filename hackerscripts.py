# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(theString, k):
    
    n = len(theString)
    # print(n)
    index = 0
    sub = ['' for i in range(n//k)]
    for x in range(n//k):
        for y in range(k):
            if (theString[index] not in sub[x]): sub[x] += theString[index]
            index+=1
        print(sub[x])
    # print(sub, len(sub), len(sub[0]))

    # initialize substring[n/k][k] that would be a two dimensional list
    # initialize buffer type list of size(k)
    

if __name__ == '__main__':
    merge_the_tools("AABCAAADA", 3)