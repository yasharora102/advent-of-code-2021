with open("day_2_data.txt", "r") as datafile:
    data = datafile.read().split('\n')
test_data=['forward 5','down 5','forward 8','up 3','down 8','forward 2']
horz=0
depth=0
for i in data:
    if 'forward' in i:
        horz+=int(i.split(' ')[1])
    elif 'down' in i:
        depth+=int(i.split(' ')[1])
    else:
        depth-=int(i.split(' ')[1])
print(horz*depth)