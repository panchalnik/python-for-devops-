#while loop
# initializer
# condition 
# increment/decrement


# i=1
# while i<=10:     #condition
#     print(i)
#     i+=1     #increment/decrement


# i=1
# while 10>=i:
#     print(i)
#     i-=1  #will give infinite values and crashes after sometime.

# i=10
# while i>=1:
#     print(i)
#     i-=1


# wap to print only even number from 10-20
# start=10 
# end=20
# while start<=end:
#     if start%2==0:
#         print(start)
#     start+=1

# i=2
# while i<=20:
#     if i%2==0:
#         print(i)   
#         i+=2 


#Print numbers from 1 to 10 using while loop.
# i=1
# while i<=11:
#     print(i)
#     i+=1

# Print numbers from 10 to 1 in reverse order.
# i=10
# while i>=1:
#     print(i)
#     i-=1


# Print all even numbers between 1 and 20.
# start=1
# end=20
# while start<=end:
#    if start%2==0:
#       print("The Even number is",start)
#    start+=1   

# Print all odd numbers between 1 and 20.
# i=1
# while i<=25:
#     if i%2!=0:
#         print(i,"is odd number")
#         i+=2


# Find the sum of numbers from 1 to 100.
# a=1
# sum=0
# while a<=100:
#     sum=sum+a
#     a+=1
#     print(sum)


# a=int(input("Enter your number :"))
# start=1
# end=20
# while start<=end:
#     if start%2!=0:
#         print("The odd number is ",start)
#     start+=1

# Find the factorial of a number using while loop.
# while a>1:
#     fact=fact*a
#     print(fact)
#     a-=1


# Print the multiplication table of a number.
# i=5
# while i>0:
#     print()

# Count the digits in a number.

# wap to print the total of even numbers from 1 to 15
# i=1
# sum=0
# while i<=15:
#     if i%2==0:
#         print("The number is even",i)
#         sum = sum+i
#         print("The sum is:",sum)
#     i=i+1
        

# wap to print whether number is palindrome or not        

# text="madam"
# copy_text=text
# rev=""
# i=len(text)-1
# while i>=0:
#     rev=rev+text[i]
#     i-=1
# if copy_text==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")    


# var1="DevOps Engineer"
# copy_var1=var1
# rev=""
# i=len(var1)-1
# while i>=0:
#     rev=rev+var1[i]
#     i-=1
# if rev==copy_var1:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# wap to check whether a number is palindrome or not

# a=12321
# abc=str(a)
# i=len(abc)-1
# rev=""
# while i>=0:
#     rev=rev+abc[i]
#     i-=1
# if rev==abc:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")        

# wap to reverse the digits 1234 output should be 4321
# a=1234
# b=str(a)
# rev=""
# i=len(b)-1
# while i>=0:
#     rev=rev+b[i]
#     i-=1
#     print(rev)


a=1234
if a%10==0:
    print(a)    


    