# user give input in f.txt

f = open("f.txt","r")
t = f.read()
if t[0]==t[1] and t[0]=='/':
    delm = [t[2]]
    s = t[4:]
else:
    delm =[',','\n']
    s = t
f.close()

lis = []
def split(s):
    k=""
    for c in s:
        if (c in delm):
            lis.append(int(k))
            k=""
        else :
            k = k + c 
    lis.append(int(k))
 


split(s)

sm=0
n_list =[]
for ele in lis :

    if(ele < 0):
        n_list.append(ele)
     
if(len(n_list)>0):
    print(n_list)
    raise Exception("negatives not allowed ",n_list) 

for x in lis :
    sm += x

print("sum :",sm)




