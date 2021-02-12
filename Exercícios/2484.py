while True:
    try:
        word = input()
        for c in range(len(word)):
            for z in range(c):
                print("", end=' ')
            for i in range((len(word)-c)):
                if i == ((len(word)-c)-1):
                    if ((len(word)-c)-1) == 0:
                        print(word[i], end='\n\n')
                    else:
                        print(word[i], end='\n')

                else:
                    print(word[i], end=' ')
    except EOFError:
        break