
# for even and odd numbers 


num=int(input("enter your number"))
if num%2==0:
  print("even muber")
else:
  print("odd number")

# voting list acc. to age 

age=int(input(" enter your age "))

if age >=0 and age<=5:
    print("go to sleep")
elif age >=6 and age <=17:
    print("go to play")
elif age >=18 and age <=75:
    print("you can go for vote")    
else:
    print("go for the rest")  


## for loop

for i in range(1) :
    print("hello world!",i)

# for without loop to find any number :-
ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,]
if 85  in ls:
    print("present")
else:
    print("absent")


# with the loop 
ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,]
n=len(ls)
for i in range(n):
    # print (ls[i])
    if ls[i]==85:
        print ("present")
        break
    else:
        print("not availabel")



#for even and odd nnumber 
ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,]
for item in ls:
    if (item%2!=0):
        print("odd ")
    else:
        print("even ")

# for even and odd nnumber with the index value 
ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,]
for i in ls:
    if (i%2!=0):
        print("odd ",i)
    else:
        print("even ",i)

# for the loop whwer we find out the value which is greater or lesser than
ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,395]
for item in ls:
    if item <+50:
        print("welcome",item)
    else:
        print("hawa ane do")


# while loop presentation
# ls=[25,41,63,96,85,74,45,8,62,12,41,32,856,96,97,395]
condition=True
while condition :
    print("WELCOME")
    quiet=input("DO YOU WANT TO QUITE IT ??  PRESS y/Y :")
    if quiet=="Y" or quiet=="y":
        condition=False






    
