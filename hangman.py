import random
life = 6
success = False
words = ('baba','bubu')
word = words[random.randrange(0,len(words))]
wordObf = ['_' for i in list(word[:])]

while life>0 and not(success):
    guess = input("Guess the letter: ")
    print('\n')
    if set(guess).issubset(set(word)):
        counter1 = 0
        for i in word:
            if i == guess: 
                wordObf[counter1] = i
            counter1+=1
        print("Good guess!")
        print("".join([i+" " for i in wordObf]))
    if wordObf == list(i for i in word): 
        print(f'\nYou did it! The word is "{word}"')
        success = True
    else:  
        life-=1
        print(f"Nope. Lifes left: {life}")
        print("".join([i+" " for i in wordObf]))