with open("day_1_data.txt", "r") as datafile:
    lst = datafile.read().split('\n')
for i in range(len(lst)):
    lst[i] = int(lst[i])
#test_lst=[607, 618, 618, 617, 647, 716, 769, 792]
lst2=[]
a=0
for i in range(len(lst)-2):
    lst2.append(lst[a]+lst[a+1]+lst[a+2])
    a+=1
increase=0
count=0
while count!=(len(lst2)-1):
    if lst2[count]<lst2[count+1]:
        increase+=1
    count+=1
    
print('increase =', increase)
