while True:
    try:
        l1 = list()
        for i in range(int(input())):
            x,y = input().split()
            l1.append([x,int(y)])
        l1.sort(key=lambda x:x[1])
        for i in range(len(l1)):
            if i != len(l1)-1:
                print(l1[i][0], end=' ')
            else:
                print(l1[i][0])
    except EOFError:
        break