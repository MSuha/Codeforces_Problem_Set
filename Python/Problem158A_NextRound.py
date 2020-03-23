def main():
    count, place = map(int, input().split())
    score = list(map(int, input().split()))
    
    if score[0] == 0:
        print(0)

    elif 0 in score and place >= score.index(0):
        print(score.index(0))

    else:
        while True:
            if place != count and score[place-1] == score[place]: 
                place += 1
            else:
                break

        print(place)

if __name__ == "__main__":
    main()