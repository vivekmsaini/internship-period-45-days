#<<<<<<<< LOOP  >>>>>>>>>>>

#loop is used to give value more than 1 hello world 10 times 
#block of codes single or multiple times used as in the loop
#whenever we use multiple tiomes 

#for , while loop are the types
#  FOR LOOP :-    when you know about the iterations 10,20,30,40 etc...
#WHILE LOOP:-     when you cant knowabout the iteration or any other condition like infinity 

#for(int i =0;i<=10:i++)
#python syntax :-     :- for i range (start,stop,jump): (next line k 4 spce bar lga kr identation maintain rakho)
#                     :-     block of codes   
#   


for i in range (1,11):
    print("hello world!"  )


for i in range (1,11):
    print("hello world!" ,i )


for i in range (11):
    print("hello world!" ,i )
    
print("for loop end")

# without loop 
ls=[25,41,63,96,85,74,45,8,62,12]
if 85 in ls :
    print ("present" )
else:
    print ("absent")
 
ls=[25,41,63,96,85,74,45,8,62,12]
n=len(ls)
for i in range (n):  
  print(ls[i])     #o-9
  if ls[i]==85:
    print ("present")
    break
  else:
    print ("absent")

ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,]
n=len(ls)
for i in range (n):
    if ls[i]<=50:
        print(ls[i])
        
    else:
        print("absent") 


ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,395]

for item in ls :
    if item<=50:
        print(item)


# WHILE LOOP :-   i=0 ( initialization )               print("welcome")=10
                  # while condition :
                  #     block of codes    

# condition =true 

i=0                        #starting point
while i<=10:                     #whwn condition is true 
    print("welcome")
    i+=1       #i=i+1        loop chalna band hojygga 


#alternativr version of while loop advance choti


condition =True
while condition :
   print("WELCOME")
   quiet= input("DO YOU WNAT TO quiet IT ? PRESS Y/y: ")
   if quiet=="Y" or quiet=="y":
    condition=False






ls = [25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,94]
#even numbers loopm (for,while, both)
for item in ls :
    if (item%2!=0):
        print("odd ")

if item % 2==0:         # even number find out 

 for i  in ls:
  if i%2==0:
    print("even number",i)
    # print("i")
  else:
    print("odd number") 

#question sum of alllist and average 

ls = [25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,94]
total_sum= sum(ls)
average=total_sum/len(ls)
print("sum of the list",total_sum)
print("average of the sumn ",average)


total_sum 

