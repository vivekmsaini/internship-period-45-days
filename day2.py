# # string

# # var =
# # a - z , A - Z , 0 - 9 , _



st="upflairs"
print(st)
print(type(st))

print(st[4:7])




st="upflairs pvt ltd jaipur rajasthan"
print(st)
print(type(st))

print(st[17:23])

print(st[-1])
print(st[7])


st="upflairs pvt ltd jaipur rajasthan"
print(st[-16:-10])

print(st[:])
#[start : ending : jump]
print(st[: :])
print(st[: :1])      #by default 1

print(st[: :2])    # jump 1 chracter because jump point is 2


print(st[: :-1])       #reverse string



st = "upflairs pvt ltd jaipur rajasthan"
st2 = "UPFLAIRS PVT LYD JAIPUR RAJASTHAN"
print(len(st))     #count no. of character 

print(st.upper())

print(st2.lower())

print(st.count('j'))    

print(st.index('f'))
print(st.replace("upflairs", "flipkart"))






# # #<<<<<<<<<<<<< LIST  >>>>>>>>>>>>>>>>

ls = [10,20.23, 410,10.2,'upflairs',True,500]
print(ls)       
print(type(ls))

student_name = ['mohit','rohit','kanak','ruchika']
print(student_name[0])
print(student_name[-1])

ls1=['A','B','C','D','E']
print(ls1[2:5])
print(ls1[-4:-1])
ls1[3] = "DON"    #for replaceing list
print(ls1)
ls1.append("I")  #end
ls1.pop()  #item remove last position

ls1.insert(2,'upflairs')
ls1.remove('E')

ls = ['a sharma','b kumar','c khana']
del ls[2]
ls2=['F','G','H']
ls1.append(ls2)
ls1.extend(ls2)

print(ls1)
ls = ['z','b','f','d']
ls.reverse()
print(ls)

ls.sort()
ls.clear()
ls.copy()

print(ls)


###  copy

ls = [25,41,63,96,85,74,852]
ls2 =ls
ls2[2]="upflairs"
print(ls)
print(ls2)
