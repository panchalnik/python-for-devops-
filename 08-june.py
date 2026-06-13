#LIST AND TUPPLE:
#7.IN-BUILT METHODS OF LIST

# emp_name=["aman","shivam"]
# new_emp="kamal"
# print(emp_name)
# #append():elements add to the last index.
# emp_name.append(new_emp)
# print(emp_name)

# emp_list=[]
# for i in range(1,11):
#     name=input("Enter your name:")
#     emp_list.append(name)
# print(emp_list)    

# emp_name=["aman","shivam"]
# emp_name.append(["ma,cdc,vg,aef,adsg,a,d,v,a,g,"])     #append mai list ke ander list banti hai wo apne ander sirf ek variable leti hai agar kuch add karna hai toh ap 
# #usko square brackets mai le aao yaha iski indexing as 2 hogi 
# print(emp_name)

# #extend
# emp_name=["aman","shiva"]
# emp_name.extend("name1")  #ye extended version hai append ka ......take care of syntax. can take bulk values.
# print(emp_name)

# #insert(position,value)
# emp_name=["aman","shiva"]
# print(emp_name)
# emp_name.insert(1, "Manisha")
# print(emp_name)

#POP means to remove
# my_list=[100,200,300,400,500,600,700]
# d1=my_list.pop()
# d2=my_list.pop()  #ye by default peeche se remove karna start kar dega agar apne mention nahi kiya hai toh.
# d3=my_list.pop(4)    #ismai apne particular indexing likh di...
# print(my_list)
# print("deleted elements are:", d1,d2,d3)
""" POP kya karta hai wo by default peeche se remove karna start kar deta hai agar apne mention nahi kiya hai toh and wo indexing dene par bhi remove
kar deta hai plus wo deleted value ko return bhi kar deta hai whereas return ke ander apko particular value deni padti hai jisko apko delete karna hai"""


#remove

# my_list=[100,200,300,400,500,600,700]
# d1=my_list.remove(600)
# d2=my_list.remove(200)  
# d3=my_list.remove(100)    
# print(my_list)
# print("deleted elements are:", d1,d2,d3)

#sorting....sorting is done among same elements........
# my_list=[10,20,30,40,2,5,4]
# my_list.sort(reverse=True)   #means decending order
# print(my_list)

# my_list=[10,20,30,40,2,5,4]
# my_list.sort(reverse=False)   #means ascending order
# print(my_list)

# my_list=[10,20,30,10,40,2,5,4]
# res=my_list.count(10)   #means ascending order
# print(res)

#CLEAR:by default puri list clear kar dega...
# my_list=[10,20,30,40,2,5,4]
# my_list.clear()
# print(my_list)





#Universal method.
# my_list=[100,200,10,300,100,500,600]
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))


#Tuple method:tuple is a data structure in python used to store unchangeable values,with comma.
#tuple are immutable and it supports slicing indexing and they can be hetrogenous and homogenous.
# t1=(100)
# print(t1)
# print(type(t1))

# t1=(100,200,300,400)
# print(t1)
# print(type(t1))

#String and its property:
str1="Python-programming"
res=str1.lower()
print(res)