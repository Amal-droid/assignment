lis_t = []
lim = int(input("enter the size of list"))
for i in range(0,lim):
    elm = int(input())
    lis_t.append(elm)
print(lis_t)
temp = lis_t[0]
lis_t[0] = lis_t[lim-1]
lis_t[lim-1] = temp

print(lis_t)





