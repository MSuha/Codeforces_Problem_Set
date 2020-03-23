def main():
    word_count = int(input())
    word = []
    while word_count:
        word = input()
        if len(word) < 11:
            print(word)
        else:
            print(word[0] + str(len(word) - 2) + word[-1])
        
        word_count -= 1

if __name__ == "__main__":
    main()