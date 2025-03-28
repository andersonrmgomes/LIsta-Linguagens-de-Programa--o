l1 = list()
aux = list()
for i in range(int(input())):
    aux = input().split()
    l1.append([aux[0],int(aux[1]),int(aux[2]),int(aux[3])])
l1.sort(key=lambda x:(-x[1],-x[2],x[3],x[0]))
print(l1[0][0])