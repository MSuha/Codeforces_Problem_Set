def main():
    loop_count = int(input())
    output = 0
    while loop_count:
        loop_count-=1
        line = input()
        if line == "++X" or line == "X++":
            output += 1
        else:
            output -= 1
    print(output)

if __name__ == "__main__":
    main()