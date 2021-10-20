# https://www.hackerrank.com/challenges/no-idea/problem

def noIdea(m,n,set1,set2):
    # get array of test-againsts
    # get set nr. 1
    # get set nr. 2
    # declare initial happiness
    set1=set(set1.split(' '))
    set2=set(set2.split(' '))
    m = set(m.split(' '))
    print(len(set1 & m)-len(set2 & m))
    



if __name__ == '__main__':
    # noIdea((3,2),(1,5,3),(3,1),(5,7))
    f = open("input03.txt", "r")
    # print(len(data.split('\n')))
    noIdea(f.read().split('\n'))
    f.close()

    # noIdea(input(),input(),input(),input())