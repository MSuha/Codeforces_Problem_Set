def main():
    stone_count = input()
    stones = input()
    count = 0
    i = 0
    while i + 1 < int(stone_count):
        stone_prev = stones[i]
        stone_current = stones[i+1]
        if stone_current == stone_prev:
            count += 1
        i += 1
    print(count)

if __name__ == "__main__":
    main()