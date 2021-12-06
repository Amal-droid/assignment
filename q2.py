x=[2,1,3,5,4]
i=0
min = x[0]
for i in range(0,4):
    if min > x[i+1]:
        min = x[i+1]
print("smallest number is",min)