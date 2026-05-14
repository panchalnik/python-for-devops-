#Nested for loop
# traversing:means you have to chalaana for loop nested loop in short apko loop chalana hai
# name="python"                          #rnage ka use hota hai sirf number printing ke liye
# size=len(name)
# for i in range(size):                                            #range use karke python ko print karwana hai
#     print(i,name[i])                                               # name[i]slicing


# name="python programming"
# size=len(name)
# for i in range(size):                                            #range use karke python ko print karwana hai
#     print(i,name[i],end=" ")                
#     # print(i,name[-1])       
# 
# 
# 
# name="python"
# size=len(name)
# for i in range(size):                                            #range use karke python ko print karwana hai
#     print(name[0])                         #jitni bar loop chalega utni bar value print hoga,loop chaleha 6 bar


# printing string without using range
# name="python"
# for i in name:
#     print(i)
# control over data: in range hume value ke sath sath indexing bhi mil rahi hai but in simple jaha hum range use nahi kar rahe waha hume indexing nahi
# mil rahi 

# var1="DevOps Engineer"
# for i in var1:
#     if i=="e":
#         continue
#     print(i,end=" ")


# wap to count all teh vowels from given string:"this is devops batch"
# a="this is devops batch"
# vcount=0
# for i in a:
#     if i=="i" or i=="e" or i=="o" or i=="a":       #if i in "aeiou"
#         print(i,end=" ")

    
# a="this is devops batch"
# vcount=0    
# c_count=0
# for i in a:
#     if i in "aeiou":
#         vcount+=1
#     else:
#         c_count+=1    
# print(vcount)        
# print(c_count)
   

# wap to print your name in reverse format        
# a="MANISHA" 
# rev=""  
# for i in a:
#     print(i,end=" ")
#     rev=i+rev       #ye line bhut khatarnak hai.....
# print(rev)    

# name="python"                          #rnage ka use hota hai sirf number printing ke liye
# size=len(name)
# for i in range(size):                                            #range use karke python ko print karwana hai
#     print(i,name[i],name)                                               # name[i]slicing

    
# wap to sum of the indices of a string : "python"
# a="python"
# b=len(a)
# print(b)
# sum=0
# for i in range(b):
#     sum=sum+i
#     print(sum)

#wap to print the factorial from 1 to 8

fact=1
for i in range(1,25):
    
 fact=fact*i
 print(f"The Factorial of number is {i}= {fact}")


# wap to print only prime number from 1 to 15


