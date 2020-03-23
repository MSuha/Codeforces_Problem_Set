def main():

    size = int(input())
    output = 0

    while(size):
        size -= 1
        if sum(map(int, input().split())) >= 2:
            output += 1

    print(output)
if __name__ == "__main__":
    main()