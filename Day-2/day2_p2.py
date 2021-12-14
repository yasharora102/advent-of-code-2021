with open("day_2_data.txt", "r") as datafile:
    data = datafile.read().split('\n')
test_data=['forward 5','down 5','forward 8','up 3','down 8','forward 2']
horz=0
depth=0
aim=0

for i in data:
    if 'forward' in i:
        horz+=int(i.split(' ')[1])
        if aim!=0:
            depth+= (int(i.split(' ')[1])*aim)
    elif 'down' in i:
        aim += int(i.split(' ')[1])
    else:
        aim-=int(i.split(' ')[1])
print(horz*depth)
