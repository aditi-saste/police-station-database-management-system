import csv
f1=open("aditi.csv","w")
wr=csv.writer(f1)
wr.writerow(['rollno','name','marks'])
record=[]
while(True):
    r=int(input("enter your rollno:"))
    n=input("enter name:")
    m=int(input("enter your marks:"))
    lst=[r,n,m]
    record.append(lst)
    ch=input("enter your choice(y/n)")
    if(ch=='n'):
        break
for i in record:
    wr.writerow(i)
f1.close()
    
