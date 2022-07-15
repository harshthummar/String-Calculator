s = input("enter string : ")
lis = []
def split(s):
    k=""
    for c in s:
        if (c==','):
            lis.append(int(k))
            k=""
        else :
            k = k + c 
    lis.append(int(k))
 


split(s)

sm=0
for x in lis :
    sm += x

print("sum :",sm)

