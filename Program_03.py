#decalartion
num = (1,2,3,4,5,6,7,8,9)
odd = 0
even = 0
#for loop
for i in num:
    if not i%2:
        even+=1
    else:
        odd+=1
#print output for number of even numbers
print("Number of even numbers:",even)
#print output for number of odd numbers
print("Number of odd numbers:",odd)