data = {'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12]}
namelist=list(data.keys())
print(namelist)


count = 0

while count < len(list(data.values())[0]):
    datalist=[]
    for i in namelist:
        datalist.append(data[i][count])
    count+=1
    print(datalist)

