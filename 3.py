# user give input in f.txt

f = open("f.txt","r")
s = f.read()
f.close()
lis = []
def split(s):
    k=""
    for c in s:
        if (c==',' or c=='\n'):
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

