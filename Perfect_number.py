#program for perfect number
print("Values >15,000 may take forever ;)")
n=int(input("Enter upper limit: "))
l2=[]
for i in range(2,n):
    l1=[]
    for j in range(1,i):
        if i%j==0:
            l1.append(j)
    if i==sum(l1):
        l2.append(i)
if (len(l2)==0):
    print("empty")
else:
    print("Perfect numbers upto",n,"are:",l2)
            

        
