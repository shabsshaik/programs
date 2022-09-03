# programs
all problem solving methods and techniques
a=[4,6,-9,-5]
for i in range(0,4):
    b=[]
    c=[]
    for i in a:
        if i<0:
            b.append(i)
        else:
            c.append(i)
print(b)
print(c)
for i in c:
    b.append(i)
print(b)
