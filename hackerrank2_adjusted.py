def noIdea(data):
    dataArray = [[words for words in lines.split(' ')]for lines in data.split('\n')]
    setTestAgainst,setA,setB = {},{},{}
    if len(dataArray) == 4:
        setTestAgainst = {}
        setTestAgainst = [set([i]) for i in dataArray[1]]
        # print([set([dataArray[1][i]]) for i in range(5)])
        setA = set(dataArray[2])
        setB = set(dataArray[3])
    print(sum([len(setA & setTestAgainst[idx]) for idx,value in enumerate(setTestAgainst)])-sum([len(setB & setTestAgainst[idx]) for idx,value in enumerate(setTestAgainst)]))
    # print(len(setA & setTestAgainst[0]))
    # print(setTestAgainst[0])

def rawInput(line0,line1,line2,line3):
    processed = line0 + '\n' + line1 + '\n' + line2 + '\n' + line3
    return processed
    



if __name__ == '__main__':
    
    # rawInput(input(),input(),input(),input())
    noIdea(rawInput(input(),input(),input(),input()))
