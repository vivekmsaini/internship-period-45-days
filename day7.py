#  <<<< FUNCTION  >>>>>>>


#ser defined function
def add_two():
    num1 = 10
    num2 = 20
    result = num1 + num2
    return result


# calling
output=add_two()
print(output)


output2=add_two()
print(output2)




def add_two(num1,num2):    # parameters
    result = num1 + num2
    return result

# calling
output=add_two(num1=25,num2=50)
print(output)

output=add_two(num1=50,num2=50)
print(output)

output=add_two(num1=250,num2=250)
print(output)


ls = [41,25,63,96,85,74,54,65,85,2,5,3,6]

def my_len(ls_input):
  count = 0
  for item in ls_input:
   count += 1
   return count
  

ls = [41,25,63,96,85,74,54,65,85,2,5,3,6]

print(len(ls))
print(my_len(ls))
output=my_len(ls_input=ls)
output = my_len(ls)
print(output)


ls = [41,25,63,96,85,74,54,65,85,2,5,3,6]
    
def average_finder(ls):
  sum=0
  for item in ls:
    total_sum=+item
    average=total_sum/len (ls)
    return average

# #calling
output= average_finder(ls)
print(output)





