# https://www.hackerrank.com/challenges/no-idea/problem

from os import terminal_size


def noIdea(data):
    dataArray = [[words for words in lines.split(' ')]for lines in data.split('\n')]
    if len(dataArray) == 4:
        # print(dataArray[0])
        setTestAgainst = {}
        setTestAgainst = [set([i]) for i in dataArray[1]]
        print([set([dataArray[1][i]]) for i in range(5)])
        setA = set(dataArray[2])
        setB = set(dataArray[3])
    print(sum([len(setA & setTestAgainst[idx]) for idx,value in enumerate(setTestAgainst)])-sum([len(setB & setTestAgainst[idx]) for idx,value in enumerate(setTestAgainst)]))
    # print(len(setA & setTestAgainst[0]))
    # print(setTestAgainst[0])



if __name__ == '__main__':
    # noIdea((3,2),(1,5,3),(3,1),(5,7))
    with open("input03.txt", "r") as f:
        data = f.read()
    # print(data)
    noIdea(data)

    f.close()

    # noIdea(input(),input(),input(),input())