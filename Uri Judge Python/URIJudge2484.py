while True:
    try:
        palavra = input()
        l = []
        for i in palavra:
            l.append(i)
        n = len(l)
        for i in range(0, len(l)):
            for j in range(i):
                print('', end=' ')
            for j in range(n):
                print(l[j], end='')
                if(j != n-1):
                    print(' ', end='')
            print('')
            n = n - 1
        print('')
    except EOFError:
        break