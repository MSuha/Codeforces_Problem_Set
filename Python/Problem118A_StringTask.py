import string

def list2Stirng(word):
    word_string = ""

    for elements in word:
        word_string += elements
    
    return word_string

def convertString(word):
    word = word.lower()
    target = []
    for index in range(0, len(word)):
        if word[index] not in ["a", "e" , "i", "y", "o", "u"]:
            target.append(".")
            target.append(word[index])
    print(list2Stirng(target))

def main():
    word = list(input().split())
    word_string = list2Stirng(word)
    convertString(word_string)

if __name__ == "__main__":
    main()
