import string

def main():
    string_1 = input()
    string_2 = input()

    string_1 = string_1.lower()
    string_2 = string_2.lower()

    if string_1 == string_2:
        print(0)
    elif string_1 > string_2:
        print(1)
    else:
        print(-1)

if __name__ == "__main__":
    main()