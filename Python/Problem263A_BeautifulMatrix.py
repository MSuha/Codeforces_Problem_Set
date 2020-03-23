def main():
    for row in range(0,6):
        col1, col2, col3, col4, col5 = map(int, input().split())
        if col1 == 1:
            print(2 + abs(2-row))
            break
        elif col2 == 1:
            print(1 + abs(2-row))
            break
        elif col3 == 1:
            print(abs(2-row))
            break
        elif col4 == 1:
            print(1 + abs(2-row))
            break
        elif col5 == 1:
            print(2 + abs(2-row))
            break
        else:
            continue

if __name__ == "__main__":
    main()