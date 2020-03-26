def main():
    word = input()

    if len(set(word)) % 2 == 1:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")

if __name__ == "__main__":
    main()