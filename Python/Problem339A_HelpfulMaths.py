def main():
    expression = input()
    length = len(expression)
    num1 = num2 = num3 = 0
    
    while length > 0:
        if expression[length-1] == '1':
            num1 += 1
        elif expression[length-1] == '2':
            num2 += 1
        else:
            num3 += 1
        length -= 2
    result = num1 * "1+" + num2 * "2+" + (num3) * "3+"
    print(result[:-1])

if __name__ == "__main__":
    main()