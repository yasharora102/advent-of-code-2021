with open("day_1_data.txt", "r") as datafile:
    lst = datafile.read().split('\n')
for i in range(len(lst)):
    lst[i] = int(lst[i])

increase=0
a=0
while a!=(len(lst)-1):
    if lst[a]<lst[a+1]:
        increase+=1
    a+=1
    
print('increase =', increase)