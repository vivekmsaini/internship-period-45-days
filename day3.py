## Tuple

tpl = (10,20,25.22,12.2,'upflairs',True)
print(tpl)
print(type(tpl))
print(tpl[2:6])    #accessing
# tpl[2] = "DONE"    #changing is not allow
# del tpl[2]          #changing is not allow
print(tpl)


# immutable
# tuple accessing allow
# deletion and insertion not allow

# ##  <<<<<<<<<<   SET   >>>>>>>>>>>>>

# immutable 
# tuple is notacessing allow
# deletion is allow(if data is not avilable in set then this is show error) 
# insertion is allow
# discared is allow (not show error........)


st = {11,88,23,41,52,65,555}

print(st)
print(type(st))          # set a immuteable data type


st = {11,88,23,41,52,65,555}
st.add(1000)
st.remove(65)
st.discard(65)
print(st)

   


st1 = {11,88,23,41,52,65,63,555}
st2 = {11,88,23,1000,2000,}
st.intersection(st2)
st1.intersection(st2)
st1.update(st2) 
print(st1)





# ####   <<<<<<<<<<<<<   Dictionary    >>>>>>>>>>>>>>>
dt = {"A":10,"B":20,"c":30,"D":40,"E":50}
print(dt)
print(type(dt))

# mutable
# accessing  (allow but by key)
# deletion (allow)
# manipulation
# insertion


dt = {"A":10,"B":20,"C":30,"D":40,"E":50}
print(dt["C"])
print(dt.keys())
print(dt.values())

dt.pop("C")
print(dt)
dt["C"] = 200
dt["F"] = 300
print(dt)


dt1 = {"A":10,"B":20,"C":30,"D":40,"E":50}
dt2 = {'F':60,'G':70,'H':80}
dt1.update(dt2)
print(dt1)


student1 = {"Name":["mohit","rohit","kaloo","pappu","baabu"],
           "Marks":[41,85,63,75,11],
           "Subject":"physics"}
student2 = {"Subject":"maths"}
student1.update(student2)
print(student1)
print(type(student2))
