# what is function in python.- 1.it means steps which are predefined and every function has their own purpose.
# 2.A FUNCTION IS A BLOCK OF INSTRUCTION/CODE WHICH EXECUTE INSIDE ITS OWN BLOCK
# 3. IT USES THE CONCEPT OF DRY MEANS DONT REPEAT YOURSELF.
#4. FUNCTION HAS TWO MAIN PARTS FIRST FUNCTIONS DEFINATION SECOND IS FUNCTION CALLING.



# HOW TO DEFINE FUNCTION IN PYTHON.
# def add():                #  (parameter)
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()                                  # (argument)

# function is divided into four categories:
# 1.tak nothing return nothing
# 2.take nothing return something.
# 3.take something return nothing.
# 4.take something return something

#parameter(para)and arguments (args)
# and para =args alwzys
#positional arguments
# def add(a,b):
#     c=a+b
#     print(c)
# add(10,20)
# add(2,5)
# add(8,15)
# add(85,25)    #function apne aap ko 1000 bar call kar sakta hai.

# write a function for formatting table    
# def table_print(n):
#     for i in range(1,11):
#         print(f"{n} x{i} = {n*i}")
# table_print(2) 
# print("❌❌❌❌❌❌❌❌❌❌")       
# table_print(5)
# print(".........................")
# table_print(10)


# using while loop
# def table_print(a):
#     i=1
#     while i<=10:
#         print(f"{a} X {i} = {a*i}")
#         i+=1
# table_print(5)        

# function banao aur usko call kar lo different outputs ke sath

# def multiplication(a,b):
#     print("multipication is ",a*b)
# multiplication(10,5)
# print(">>>>>>>>>>>>>>>>>>>")
# multiplication(20,5)
# print(".....................")

# def division(a,b):
#     print("division is :",a//b)          #using here floor division
# division(15,3)
# print("...............")
# division(25,3)

# def subtraction(a,b,c=0):
#     print("subtraction is ",a-b)
# subtraction(50,20)
# print(">>>>>>>>>>>>>>>>>>") 
# subtraction(20,50)   

# alag tareeke se likho abs

# def add(a,b):
#     print("Addition is:", a+b)

# def mul(a,b):
#     print("multiplication is :",a*b)

# def div(a,b):
#     print("division is:",a//b)

# def sub(a,b):
#     print("subtraction is :", a-b)    

# option=input("choose from : +,-,*,//:")    
# if option=="+":
#     add(10,20)
# elif option=="//":
#     div(20,10)    
# elif option=="-":
#     sub(20,10)
# elif option=="*":
#     mul(10,20) 

# else:
#     print("contact dev sir")           


# IN PYTHON BY DEFAULT FUNCTION RETURN GIVES NONE.

# def add(a,b):
#     return "hello"                    
#     return "djkaghiu"
# res=add (2,3)
# print(res)

# def add(a,b):
#     return a+b
# res=add(10,20)
# print(res)
# add(10,20)
# def sub(a,c):
#     return a-c
# print(sub(10,res))

# function greet
# def greet(a):
#     return a
# i=greet("Hello")
# def user_name(a):
#     return a
# p=user_name("sudhir")
# def greet(a):
#     return ("Sudhir is paglet")
# x=greet("Sudhir is paglet")
# print(i,p)
# print(x)

# waf to check the function pass by arguments whether it is odd or even

# def num(a):
#     if a%2==0:
#         print("The number is even:",a)
#     else:
#         print("The number is odd:",a)

# num(3)            
# num(2)
# num(10)
# num(5)

# def num(a):
#     pass
# num(4)

# waf to check which number is greater and two numbers pass by user.
# def num(a,b):
#     if a>b:
#         print(a,":number a is greater")
#     else:
#         print(b,":number b is greater")    
# num(10,20)        
# num(50,40)

# WAF to check a character pass by user is vowel or consonant
# def char(a):
#     if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#         print("vowel")
#     else:
#         print("consonant")
# # a="x" 
# a="i"     
# char(a)                  

# def char(a):
#     if a in "aeiouAEIOU":
#        return "True"
#     else:
#        return "False"
# x=char("a")    
# print(x)

# NOW WE WILL return
# WAF TO CHECK IS NUMBER COMPLETELY DIVIDED BY 2 AND 3 AND RETURN MESSAGE YES NUMBER IS COMPLETELY DIVISIBLE AND IF NOT THAN NO

# def num(num):
#     if num%2==0 and num%3==0:
#         print(num,"Number is completely divisible")
#     else:
#         print(num,"Number is not divisible")

# num(6)
# num(9)
# num(20)

# def num(a):
#     if a%2==0 and a%3==0:
#         return"a ,divisible"
#     else:
#         return"a ,not divisible"
# res=num(7)    
# print(res)


# waf to return length of a string pass by user without using length method.
# def len_string(a):
#     c=0
#     for i in a:
#         c+=1
#     return c    

# res=len_string("python")
# print(res)


# def char(a):
#     if a in "a,e,i,o,u,A,E,I,O,U":
#        return "True"
#     else:
#        return "False"
# # x=char("a")    
# # print(x)


# waf to check how many vowels in a given string
# vcount=0
# def vowel_count(a):
#    c=0
#    for i in a:
#       print(i)     
#       if i in "AEIOUaeiou":
#          c+=1
#    return c         
#                                                     #pass laga kar program shuru karo
# res=vowel_count("programming")
# print(res)



# write consonant
# def count_c(a):
#    c=0
#    for i in a:
#       print(i)
#       if i in "AEIOUaeiou":
#          print("No consonant")
#       else:
#          c+=1
#    return c

# res=count_c("My name is Manisha")
# print(res)

#LOCAL VARIABLE -PRESENT INSIDE FUNCTION VS GLOBAL VARIABLE-PRESENT OUTSIDE FUNCTION AND U HAVWE TO DEFINE IT
# AS GLOBAL OUTSIDE FUNCTION
# KISI LOCAL VARIABLE KO GLOBALLY ACCESS KARNA HAI TOH USKO INSIDE GLOBAL KARKE DEFINE KAR DO

# name="DEV"               #global
# def msg():
#    print("inside:",name)
# msg()
# print("outside:",name)   


# def msg():
#    name="DEV"                                #local
#    print("inside:",name)
# msg()
# print("outside:",name)    #isko koi global wala chahiye kyuki wo name toh function ke ander define hai


# def msg():
#    global name
#    name="DEV"                             
#    print("inside:",name)
# msg()
# print("outside:",name)


# waf to count char p in" python programming" return total occurence

# def count_char(a):
#     print(a)
#     count=0
#     for i in a:
#         print(i)
#         if i=="p":
#             count+=1
#     return count        
# res= count_char("python programming")
# print(res)

#  waf to return sum of string indices "python"
# def indices_sum(a):
#    print(a)
#    sum=0
#    for i in range(len(a)):                 #range use karo indices ke liye
#       print(i)
#       sum=sum+i
#    return sum
      
# x=indices_sum("python")
# print(x)






