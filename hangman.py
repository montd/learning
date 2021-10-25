import random
import urllib.request

# Variables
gallowsSegments: int = 6
wordSite = 'https://www.mit.edu/~ecprice/wordlist.10000'

def debug(*argv):

    for arg in argv:
        print(arg)
    return

class Message:
    def __init__(self) -> None:
        pass

    def success(wordObf) -> None:
        print("Good guess!\n" + ''.join([i+" " for i in wordObf]))

    def mistake(gs, wordObf) -> None:
        print(f"Nope. Gallows Segments left: {gs}")
        print("".join([i+" " for i in wordObf]))

    def win(word) -> None:
        print(f'\nYou did it! The word is "{word}"')
    
    def lose(word) -> None:
        print(f"\nThe word was: {word}")
    
    def printHiddenWord(wordObf):
        print("".join(["_"+" " for i in wordObf]))

def getWord(wordSite) -> bool:
    try:
        response = urllib.request.urlopen(wordSite)
    except urllib.error.HTTPerror as e:
        print("Sorry, a HTTP error occured. The game will exit now.")
        return False
    except urllib.error.URLError as e:
        print("Sorry, a URL error occured. The game will exit now.")
        return False
    else:
        long_txt = response.read().decode()
        words = long_txt.splitlines()
        return words[random.randrange(0, len(words))]

def guessing(gallowsSegments, word):
    success = False # Init
    wordObf = ['_' for i in list(word[:])]
    Message.printHiddenWord(word)
  
    while gallowsSegments > 0 and not (success):
        guess = input("Guess the letter: ")
        print('\n')

        if set(guess).issubset(set(word)):
            _c1 = 0
            for i in word:
                if i == guess:
                    wordObf[_c1] = i
                _c1 += 1
            Message.success(wordObf)

        else:
            gallowsSegments -= 1
            Message.mistake(gallowsSegments,wordObf)

        if wordObf == list(i for i in word):
            Message.win(word)
            success = True

    if not (success):
        Message.lose(word)
    return


def main():
    word = getWord(wordSite)
    if (word == False): 
        return None
    
    guessing(gallowsSegments, word)
    return


if __name__ == "__main__":
    main()
