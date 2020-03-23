def main():
    teams = input()
    if ("0000000" in teams) or ("1111111" in teams):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()