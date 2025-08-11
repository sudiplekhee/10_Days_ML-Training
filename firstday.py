# # #This is the first comment
# # #adding two number
# # """This is multiline comment"""

# # #Variables
# # a=5
# # b=6
# # c="python"
# # print(a,b,c)
# # a=10 #This is integer
# # b"StudyGlance" #This is string
# # c=3.13 #This is float
# # print(a)
# # print(b)
# # print(c)
# # x,y,z=20,10,2
# # print(x,y,z)
# # a,b,c=50,12,2
# # print(a,b,c)
# # a=100
# # b=10.22
# # c="python"
# # d=True
# # print(type(a),type(b),type(c),type(d))

# # a=6+7j #This is complex class
# # print(type(a))

# # #write a program to add two complex number and also print the type of the result obtained
# # a=555+6j
# # b=666+5j
# # sum=a+b
# # print(sum,type(sum)) 

# # #type casting
# # a=6
# # print(type(a))
# # print(type(str(a)))

# # p="python"
# # print(type(int(p)))
# b=1234
# print(type(str(b)))

# a=int(input("Enter the value of a:"))
# print(f"The value of a is {a}")

# #wap a program to take the two values from user and print its power
# a=int(input("Enter first value:"))
# b=int(input("Entersecond value:"))
# results=a ** b
# print(f"The power of both the number is {results}")
# a=50
# b=6
# print(a==b) #True return
# print(a != b) #Return false
# print(a>b)

# #wap to program to check whether a given number is odd or even

# a=int(input("Enter number:"))
# if a%2==0: #kunai pani number zero sanga equal cha vane tyo even vanera print huncha natra odd huncha
#     print("This is even number")
#     print(f"{a} is even")
# else:
#     print("This is odd number")
#     print(f"{a} is odd ")
 
#write a program to check the mark if mark >=80 disctiction , 70 <=mark <80 --> First division
#mark 60<=mark<70 ---->second division\
#mark 50<=mark<60 ---->third division
#else pass
# marks=int(input("Enter marks:"))
# if marks >=80:
#     print(f"{marks} is disctinction")
# elif 70 <=marks <80:
#     print(f"{marks} is first division")
# elif 60<=marks<70:
#      print(f"{marks} is second division")
# elif 50<=marks<60:
#      print(f"{marks} is third division")
# else:
#     print("Just passed")
# for i in range(0,10):
#     print(i,end=" ")
# i=1
# while(i<=10):
#     print(i)
#     i = i+1
# else:
#     print("Loop terminated")

# for i in range(5):
#     print("Hello",i) #i halim vane tya 0 index dheki 4 index samma print huncha
    
# for i in range(1,10):
#     print("Hello",i)

#wap a program to print the even number between 1 to 20

# for i in range(1,20):
#     if i%2==0:
#         # print(f"{i} is even number")
#         print(i,end=" ")
    # else:
    #     print(f"{i} is odd number")


#while loop
# i=1
# while i<=19:
#     print(i,end=" ")
#     i +=1

age=int(input("Enter your age:"))
while age<1 or age>100:
    print("This is not valid")
    age=int(input("Enter your age:"))
else:
    print("age is valid")
    
#break statement
# for i in range(10):
#     if i == 6:
#         # break
#         continue  #continue halim vane jun i==6 rakhim 6 matra skip garcha
#     print(i)



 