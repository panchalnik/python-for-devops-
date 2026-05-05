# type casting and type coversion
# a=10
# b=10.5
# print(a+b)
# float is greater than integer

# num="100" ye abhi string hai aur coma hata kar int ban jaega
# name="NIk"
# print(num+" "+name)
# print(type(name))
# print(type(num))

# typecasting
# var1=float(100)
# print(type(var1))
# print(var1)

# num1="50"
# num2="100"
# res=int(num1)+int(num2)
# print(res)
# res1=str(num1)+str(num2)
# print(res1)
# print(type(res1))
# res2=float(num1)+float(num2)
# print(res2)

# x='3.5'
# print(int(x)) string ko na ap float mai convert kar sakte aur na hi int mai
# input() by default str print krta hai
# string*string=utne times ho jata hai for example 'hello'*3
# str='hello' note : string string concatenate hote hai string aur number concatenate nahi krte
# print(st)
# x='3.5'
# print(int(x))

 
# x='10'
# y='2'
# print(x*int(y)) ye note karo ke ye power mai chala jaega
 
# x='35'
# print(float(x)) 

# x=input()
# y=5
# print(x+y)

# student_name="Manisha Panchal"
# student_address="85 Maliwara Ghaziabad ,UP-201001"
# student_number="+91 9654448520"
# # how to validate matlb uski length kitni hai 10se jyada tho nahi hai
# print(len(student_number)) 
# # aap len se length check kar sakte ho aur length sirf string ki check kar sakte hai
# student_profile="""Hello I am suchita 
# and i am a devops engineer looking for a good opportunity
# so that i can see the world"""
# # if you want multi line string then place them in double or single triple quote.
# print(student_profile)
# # agar string mai kuch highlight karna hai toh usko quotes mai daal do lekin dhyan dena jo quote bahar use kiya hai usko ander nahi use karna 
# student_profile1="""Hello I am suchita 
# and i am a 'devops engineer' looking for a good opportunity
# so that i can see the world"""
# print(student_profile1)
# student_profile2="""Hello I am suchita {student_name}
# and i am a 'devops engineer' looking for a good opportunity
# so that i can see the world"""
# print(student_profile2)
# student_profile3=f"""Hello I am suchita {student_name}
# and i am a 'devops engineer' looking for a good opportunity
# so that i can see the world and my address is {student_address}"""
# print(student_profile3)
# agar aap string formating use karte ho string se phle toh wo particular value dega string ki

# operators in Python
# 1.Arithmatic opr
# 2.Assignment opr
# 3.Comparison/relational opr
# 4.logical operator
# 5.Membership operator
# 6.Identity opr
# 7.Bitwise opr

# Assignment operator it is just a way of assigning a value to a variable.
# a=10
# a=a+10
# a+=10  
# a-=10
# a*=10
# print(a)
# it will take final value of a or the last or updated value of a

# 3.Comparison (>,<,>=,<=,==,!=)
n1=30
n2=40
# print(n1!=n2) this symbol denotes not equal to ....output will be in boolean 

# str1="A"
# str2="a" 
# print(str1>str2) 
# inki ASCII value se compare karenge

# str1="Aman" capital letters ki value kam hoti hai as compared to small letters
# str2="aman kumar" inke first letter ki ASCII value lenge
# print(str1>str2)

# 4.logical opr(and,or,NOT)
# n1=1
# n2=3
# res=n1==1 and n2==3 her we are using and operation similarly we can use or and not operation.
# print(res)

