# 6.identity opr (Id) (is/ is not) -used to check address of input and mostly numbers ke liye use kiya jata hai 
# character par bhi use hota hai but numbers par jyada use hota h 
# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is b)

# a=10 
# b=100
# print(id(a))
# print(id(b))
# print(a  is b)
# print(a is not b)
    
# conditional statement (decision making like -usko intelligent banane ka)
# a=100
# b=1000
# c=1000
# if a==b and b==c:     
#     # idhar maine comparison kiya hai assign nahi kiya
#     print("The address is same")
# else:
#     print("The address is not same ")    
# if   a==b or b==c:    
#      print("The address is same")
# else:
#     print("The address is not same ")     


# a=2       #agar a defined nahi hota toh wo by default 0 leta and o is considered as false in computer language.
# if a:
#     print("yes")
# else:
#     print("no")       


# a1=0
# if a1:
#     print("yes")
# else:
#     print("no")       
# # # ye hamesha 0 and 1 ko hamesha true aur false ke terms mai consider karega


# if True*0:            #yaha par True ko 1 considder karenge
#     print("yes")
# else:
#     print("no")    


# wap to check number given by user in odd or even.
# a=int(input("Enter your number:"))
# if a%2==0:
#     print("The given number is even")
# else:
#     print("The given number is odd")    
    
# wap a program to print the last digit of number is 456735
# num=int(input("ENter your number:"))
# remainder=num%10
# if num%10==0:
#     print(0)
# else:
#     print(remainder)

# num1=3
# num2=9
# num3=12
# # wap to find largest
# # wap to find smallest
# if num1<=num2 and num1<=num3:
#     print("The smallest number is:",num1)
# else:
#     print("The largest number is:",num2)


# num1=3
# num2=9
# num3=12
# # wap to find largest
# # wap to find smallest
# if num3>=num2 and num3>=num1:
#     print("The smallest number is:",num1)
# else:
#     print("The largest number is:",num3)



# num1=31
# num2=9
# num3=12
# if num1>=num2 and num1>=num3:
#     print(f"{num1} is greatest")
# if num2>=num1 and num2>=num3:
#     print(f"{num2} is greatest")
# if num3>=num1 and num3>=num2:
#     print(f"{num3} is greatest")       
# if num1<=num2 and num1<=num3:
#     print(f"{num1} is smallest")
# if num2<=num1 and num2<=num3:
#     print(f"{num2} is smallest")
# if num3<=num1 and num3<=num2:
#     print(f"{num3} is smallest")      

#aap multiple conditions ke liye continuous if statement chala sakte ho.  
# ye multiple if ki condition hai, tho har output check hoga aur jo bhi sahi hoga sb print hoga',multiple if means multiple output.

# n=100
# if n>500:
#     print("yes1")
# if n>50:
#     print("yes2")    
# if n>70:
#     print("yes3")
# if n>120:
#     print("yes4")

# else:
#     print("No")

# remember else hamesha sirf last wale ke liye kam karega
# aur multiple if har condition ko check kaega whether it is right or wrong ....bargainiong karke sasta samamn laega


# elif condition - mila jula ke output ek hi aaega
    #  jaha bhi true condition millli wahi program terminate ...lekin multiple if mai esa nahi hai
n=100
# if n>500:
#     print("Yes1")
# elif n>60:
#     print("Yes2")
# elif n>70:
#     print("Yes3")        
# # else:
    # print("No")    #yaha ye else phle wala if ke liye hai ,,,agar ap else  part hata deta ho else if mai toh+ aur sari condition 
#     #false hoti hai then koi output nahi aaega.


# o7/may
# nested if else
# name=" "
# if name=="Dev":
#     print("Yes name is provided")
# else:
#     print("Name is not provided")    
    
# name="aman "
# if name:                 #because name is already mentioned earlier .
#     print("Yes name is provided")
# else:
#     print("Name is not provided")    


# name="aman"  #if name is removed then output is name is not provided. wo pura if statement hi wrong ho jaega tho directly else part par aajaega.
# if name:  # this means name ki value exists karti h              #because name is already mentioned earlier .
#   print(f"Yes {name} is provided")
#   address="Noida"
#   if address:
#      print(f"Yes address is {address} provided")
#   else:
#      print("Address is not provided")   
# else:
#     print("Name is not provided")    
# print(id(name))

#with the help of conditional statement we are making our program smart.

# num1=20
# if num1%2==0:
#     print("EVEN")
#     mob=input("Enter your number:") 
#     country_code=int(input("Enter your country code:"))
#     print(mob)
#     if len(mob)==10 and country_code==+91:
#         print("valid number")
#     else:
#         print("Invalid number")    
# else:
#     print("ODD")    


pre_marks=int(input("Enter your pre marks: "))
if pre_marks>=400:
    print("You are eligible for mains exam")
    mains_marks=int(input("Enter your mains marks:"))
    if mains_marks>=700:
        print("Congratulations your are eligible for interview")
    else:  
        print("sorry your are not eligible for interview")
    interview_marks=int(input("Enter your interview marks :"))
    if interview_marks>=250:
        print("congratulations, wait for the merit list") 

    total_marks=mains_marks+ interview_marks
    if total_marks>=950:
        print("conjgratulation you are selected")

    else:
        print("Better luck next time,❌❌")

    
else:
    print("sorry, Better luck next time ❌❌")


  


























































