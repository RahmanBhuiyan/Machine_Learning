a=['High school',"Bachelors","Masters","Diploma"]
b={'High school':0,"Diploma":1,"Bachelors":2,"Masters":3}
k=[]
for x in range(len(a)):
    z=b[a[x]]
    k.append(z)
print(k)
