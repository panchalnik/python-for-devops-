# loops in python
# 1.for loop:ranged based
# 2.while loop:condition based

# for loop to repeat 
# print("Aman"*100)    #without loop

# for i in range(100):    #a-z we cAN use anything but mostly we use i,j,k and _(lekin underscore bass loop ko chalane ke liye hai
    # sirf uska syntax complete karne ke liye )
    # print("Aman")

# range has three parameter(start:0,stop-1,step:1)  step means one step at a time and step by default is 1.
# range always works with integer number
# for i in range(5):
#     print(i)

# for i in range(1,5,2):     #here 2 is step menas 2 ka increment
    # print(i)   

# for i in range(2,8,10):  
#     print(i,end=" ")

# for i in range(1,10,1):
    # print(i,end=" ")         #end command for horizotal series.

# for i in range(1,20):
#     if i==10:
#         break    #program break at 10
#     print(i,end=" ")    

# for i in range(1,20):
#     if i==10:
#         continue
#     print(i,end=" ")    

# for i in range(1,40):
#        if i%2==0:
#             print(i,end=" ")

# for i in range(2,50):
#       if i%2 !=0 :
#             print(i,end=" ")      
#       else:
#         print(f"even :{i}")             

# s=0
# for i in range(1,5):
#     s=s+i
#     print(s)
# print(s)


# s=1
# for i in range(1,5):
#     s=s*i
#     print(s)
# print(s)



# for r in range(10,1,-1):
    
#     print(r)

# for r in range(10,15,-1):
#     print(r)   #invalid aap ulta nahi ja sakte 10 se 15

# wap to takes start point and end point from user input and print all numbers divisible by 2 and 3.
# start=int(input("Enter the start point:"))
# end=int(input("Enter the End point:"))
# print("start point is:",start)
# print("End point is:",end)

# print("Numbers divisible by 2 and 3 are:")

# for i in range(start,end+1):
#     if i%2==0:
#         print("Number is divisible by 2:",i)
#     else:
#         if i%3==0:
#             print("Number is divisible by 3:",i)    


#wap to take a number from user input and print formated table.
# 3x1=3
# 3x2=6
# 3x3=9 ...........


# wap to take a number from user input and print reversed formated table.
# 3x10=30
# 3x9=27
#nested loop

# for i in range(1,6):
#     print(i,"first loop")
#     for j in range(1,6):
#         print("inner loop")
#         for k in range(1,6):
#             print(i,"chota loop")


# emp_name=["aman","kamal","nilesh","raju"]
# print(emp_name[0],end=" ")

# for i in emp_name:
#     print(i,end=" ")




