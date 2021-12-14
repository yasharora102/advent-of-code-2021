with open("day_3_data.txt", "r") as datafile:
    data = datafile.read().split()
with open("day_3_data.txt", "r") as datafile:
    data2 = datafile.read().split()


test_list=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
test_list2=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

def oxygen(data):
    length=range(len(data))
    bin_length=len(data[0])-1
    b=0
    a=0
    for x in length:
        lst_1=[]
        lst_0=[]
        if b>bin_length:
            break
        if a>bin_length:
            break
        for i in data:
            if i[b]=='1':
                lst_1.append(i[b])
            else:
                lst_0.append(i[b])
        if len(lst_0)!=0 and len(lst_1)!=0:
            if len(lst_1)>len(lst_0):
                rem_index=[]
                for j in data:
                    if j[a]=='0':
                        rem_index.append(data.index(j))
                for k in sorted(rem_index,reverse=True):
                    data.pop(k)
                
            elif len(lst_1)==len(lst_0):
                for j in data:
                    if j[a]=='0':
                        data.remove(j)
                
            else:
                rem_index=[]            
                for j in data:
                    if j[a]=='1':
                        rem_index.append(data.index(j))    
                for k in sorted(rem_index,reverse=True):
                    data.pop(k)
           
        a+=1
        b+=1
    return data

def co2(data2):
    c,d=0,0
    length2=range(len(data2))
    bin_length2=len(data2[0])-1
    for x in length2:
        lst_1=[]
        lst_0=[]
        if d>bin_length2:
            break
        if c>bin_length2:
            break
        for i in data2:
            if i[d]=='1':
                lst_1.append(i[d])
            else:
                lst_0.append(i[d])
        if len(lst_0)!=0 and len(lst_1)!=0:
            if len(lst_1)>len(lst_0):
                rem_index=[]
                for j in data2:
                    if j[c]=='1':
                        rem_index.append(data2.index(j))
                        
                for k in sorted(rem_index,reverse=True):
                    data2.pop(k)
                
            elif len(lst_1)==len(lst_0):
                rem_index=[]
                for j in data2:
                    if j[c]=='1':
                        rem_index.append(data2.index(j))
                        
                for k in sorted(rem_index,reverse=True):
                    data2.pop(k)
                
            elif len(lst_1)<len(lst_0):
                rem_index=[]            
                for j in data2:
                    if j[c]=='0':
                        rem_index.append(data2.index(j))   
                for k in sorted(rem_index,reverse=True):
                    data2.pop(k)   
        c+=1
        d+=1
    return data2

oxy_list_val=oxygen(data)
co2_list_val=co2(data2)
o='' 
oxy_bin=o.join(oxy_list_val)
oxy_dec=int(oxy_bin,2)
co=''
co2_bin=co.join(co2_list_val)
co2_dec=int(co2_bin,2)

print(oxy_dec*co2_dec)

