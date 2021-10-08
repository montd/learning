import random
import urllib.request

def debug(*argv):
    for arg in argv: print(arg)
    return

def guessing(life, word):
    wordObf = ['_' for i in list(word[:])]
    success = False
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
        else:  
            life-=1
            print(f"Nope. Lifes left: {life}")
            print("".join([i+" " for i in wordObf]))
        if wordObf == list(i for i in word): 
            print(f'\nYou did it! The word is "{word}"')
            success = True
    if not(success): print(f"\nThe word was: {word}")        
    return

def main():
    life = 6
    wordSite = 'https://www.mit.edu/~ecprice/wordlist.10000'
    response = urllib.request.urlopen(wordSite)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    word = words[random.randrange(0,len(words))]
    debug(response, word)


    guessing(life, word)
    return



if __name__ == "__main__":
    main()