with open("day_3_data.txt", "r") as datafile:
    data = datafile.read().split()
print(data)

test_list=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
b=0
gamma=[]
epsilon=[]
for x in range(len(data)):
    lst_1=[]
    lst_0=[]
    if b>(len(data[0])-1):
        break
    for i in data:
        if i[b]=='1':
            lst_1.append(i[b])
        else:
            lst_0.append(i[b])
    if len(lst_1)>len(lst_0):

        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0') 
        epsilon.append('1')       
    b+=1
g=''
e=''
gam_value_bin=g.join(gamma)
ep_value_bin=e.join(epsilon)
gam_value_dec_=int(gam_value_bin,2)
ep_value_dec=int(ep_value_bin,2)
print(gam_value_dec_*ep_value_dec)

