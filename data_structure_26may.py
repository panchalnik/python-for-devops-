# DATA STRUCTURE 

# DATA STRUCTURE USED TO STORE DATA EFFECIENTLY AND MAKE FASTER ACCESS, LIKE FOR OPERATIONS LIKE READ AND WRITE.
# 1.list : list()
# 2.STRING : str
# 3.DICTIONARY : dict()
# 4.SET :set()
# 5.TUPLE: tuple()

# 1.LIST: list is a data structure in python used to store multiple data of different types in one variavle.
# list ke ander ke data ko element bolte hai 
# ex: marks_10th=[20,55,10,12,25,30]         is list mai 6 element hai

# list can define by using square bracket[] and data inside it is known as elements.
# list can be heterogenous and homogenous.
# list are mutable (changeble) and strings are immutable.
# ex:
# marks=[20,55,10,"hello",2.5,"my name is anthony"]
# print("before update:",marks)
# marks[0]=200            #value changed means mutate kiya hai..
# marks[-1]=400
# marks[-2]=500-30
# print("After update:",marks)
# print(len(marks))
# total index = length -1
# list supports indexing,slicing and follows ordering sequence.

# *list and its peoperty-----------------------------------------------------------------28-05-1993--------------------------------------------------------------
# 1.creation of list.
# 2.updati0n of list
# 3.Indexing
# 4.slicing
# 5.Traversing
# 6.In-built methods
# 7.test
# 8.Assignments

#SLICING...........U CAN CUT ANY PART OF YOUR LIST THAT COMES UNDER YOUR SLICING.
# marks=[10,20,30,40,50,60,70,80]
# stop mai jo likha hai usse ek kam kar do 
# [start (0):stop-1:step(1)]   start by default zero hota hai and step bhi by default 1 hota hai ....aur stop ek kam chalta hai & bydefault 0 hota h wo hum apne samajhne ke liye
# -1 laga dete hai
# sub_list=marks[0:6]
# sub_list=marks[3:5]
# sub_list=marks[0:8:2]   #and start khud ko include karta hai.
# sub_list=marks[8:4:-2]    #negative mai hamesha pehle jyada value baad mai kam value kyuki wo ulta chal raha hai 
# sub_list=marks[6::-3]
# sub_list=marks[:-1]
# sub_list=marks[:-4]
# sub_list=marks[:]     #puri row as it is print ho jaegi.
# sub_list=marks[::-1]   
# sub_list=marks[2:0]     #not possible
# sub_list=marks[2:0:-1] 
 #yaha 2 se 0 tak jana hai...kaise jaoge - karke hi jaoge na...ab zero ki position stop hai tho zero se ek kam jaega and ulta jana h bcoz of -1
# sub_list=marks[5:0:-1] 
# # sub_list=marks[::] 
# sub_list=marks[:3:-1] 
# sub_list=marks[:5:-1] 
# sub_list=marks[:5:-2] 
# sub_list=marks[:4:-2] 
# sub_list=marks[:5:-1] 

# print(sub_list)

# 6.Traversing
# marks=[10,20,30,40,50,60,70,80]
# for i in range(len(marks)):    #ye sirf numbering dega i in range

#     print(i,marks[i])        #ye sirf marks[i] exact value dega


# marks=[10,20,30,40,50,60,70,80]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This elm is even :{marks[i]}")
#     else:
#         print(f"this elm is odd :{marks[i]}")


# marks=[10,20,30,40,50,60,70,80]
# for i in marks:
#     print(i)  
#     if i%2==0:
#         print(f"this elm is even:{i}")


# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# total=0
# for i in marks:
#     total=total+i
# print(total)

# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# total=0
# for i in range(len(marks)):
#     total=total+marks[i]
# print(total)    



# wap to swap the first value of list with last value of list
# a=[10,20,30,40,50,60,70,80]
# print("Initially the list was",a)
# c=a[0]
# a[0]=a[7]
# a[7]=c
# print("The list after conversion becomes",a)


# wap to find the sum of the all elements in the list
# a=[10,20,30,40]
# s=0
# for i in a:
#     s=s+i
# print(s)    

# sum of omly even element and only odd elements
# a=[10,20,30,40,55,75,85]
# sum=0
# for i in a:
#     # print(i)
#     if i%2==0:
#         sum=sum+i
#         print(sum)    
    

# sum of only odd numbers in list:    
# a=[10,3,4,6,22,31,35,55,40]
# sum=0
# for i in a:
#     if i%2!=0:
#         sum=sum+i
# print("The sum of odd numbers:",sum)

# wap to find the count of no.of int values and how many strngs are there
a=[70,"aman",50,10,20,"rohan","iq-india"]
c_int=0
c_str=0
for i in a:
    if type(i)==int:
        c_int+=1
    elif type(i)==str:
        c_str+=1
print("The integer count is :",c_int )
print("The string count is :",c_str)

