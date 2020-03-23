from math import ceil

def countStone(short_edge, long_edge, square_edge):
    print(int(ceil(short_edge/square_edge) * ceil(long_edge/square_edge)))

def main():
    s_edge, l_edge, square = map(float, input().split())
    countStone(s_edge, l_edge, square)

if __name__ == "__main__":
    main()