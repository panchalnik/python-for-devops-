# print("hello nikki")
# print(17*15)
# print("Hey I am a good girl \n and this viewer is also a good person") 
# # this is an escape sequence character (ek esa character jisko aap directly use nahi kr sakte )jo hamari statement ko nayi line se likhta hai 
# print("I am going to be a successful person soon")
# ''' triple single quote mai multiline comment daal sakte ho'''
# print("Hey I am a \"good girl\" \n and this viewer is also a \"good person\"") 
# # agar apko quotes ke ander quotes use krne hai apni statement mai then aap \" ko use karo usse apka particular term highlight ho jaega
# print("hey",6,7,)
# print("hey",6,7, sep"~", end= )
# a="12"
# b="52"
# print(int(a)+int(b))
# print(a+b)

# system har input ko as a string leta hai unless ap usko defina na karo

# a=input("enter your number")
# b=input("enter your second number")
# print(a+b)
# print(int(a)+int(b))

# you cannot put double quotes into double quotes it will give you error
# triple single quotes ke ander aap multiple lines print karwa sakte wo as a string act karegi u can write anything in it.
# a='''he said, i am your friend
# and i live in ghaziabad that is just 20kms
# away from your location,so if u are free can we meet.'''
# print(a)
# print()
# print(-------------------)
# print(😂😂😂😂😂)
      
#     #   idhar error ye hai ki maine print ke ander "" nahi use kiya tha tabhi wo error aa raha tha

# fruit="Mango"
# print(fruit[0:3])
# print(len(fruit))  #len is used to find length of string
# [0:5] this print the exact value placed on that
# agar len negative given hai then aap usko string ki length se subtract karke exact value daal do
  
# immutable matlb you cannot change aap string ko inplace change
# nahi kar sakte par aap uski ek copy banasakte ho ....
# string are immutable  

# a="!!!!!Manisha!!!!!!"
# print(len(a))
# print(a.upper())   #converts string in upper case ye ourani 
# # ko change nai karega infact nayi string bana dega
# print(a.lower())
# # print(a.rstrip)
# # lecture 13 of code with harry

 #wap to write good morning sir
# Time=int(input("Enter your timing:"))
# if Time<=12:
#     print("GOOD MORNING")
# else time:
#     print("good afternoon")

#loop
# name="Abhishek"
# for i in name:
#     print(i)
#     if (i=="s"):
#         print("s stands for shakira shakira")

# i is line se ek k nneche ek print karwa do

# colors=["Red","green","blue","yellow","white"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# range in for loop
# for k in range(5):
#     print(k)
# for k in range(50):
#     print(k)    

# # output hamesha zero se aaega lekin agar aap 1 se
# # print chahte ho toh print mai k+1 daal do
# print(k+1)

# for k in range(1,10):   #range define karne par hamesha ek pt kam jaega.
#     print(k)

# for k in range(1,100):
#     print(k+1)    

# for k in range(1,15,3): #jab aap teen words ko involve karte ho toh third factor important role play karta h
#     print(k)  

#while loop
# i=0
# while(i<4):
#     print(i)
#     i=i+1
# print("Done with the loop")    

# i=int(input("Enter your number :"))
# while(i<=5):
#     i=int(input("Enter your number :"))
#     print(i)

# print("I am done with the program")

# fruit="Mango" 
# print(fruit[:])#called slicing of string

# print(fruit.upper())
# print(fruit.lower())
# print(fruit.replace("Mango","lichi"))

# a="introduction to python"
# print(a.capitalize())
# print(a.center(50))
# print(len(a.center(50)))
# print(a.count("to"))

