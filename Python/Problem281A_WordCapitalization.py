import string

def main():
    word = input()
    if ord(word[0]) > 64 and ord(word[0]) < 91:
        print(word)
    else:
        print(word[0].upper() + word[1:])

if __name__ == "__main__":
    main()