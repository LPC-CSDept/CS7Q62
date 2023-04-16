

def getPrimeNumber(begin, end):
    ##################################################
    # Code your program here
    ##################################################


def main():
    begin = int(input('Enter the number for starting of range: '))
    end = int(input('Enter the number for end of range: '))
    gen = getPrimeNumber(begin, end)

    print(list(gen))


if __name__ == '__main__':
    main()
