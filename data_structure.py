# s1="this is a first string"
# s2="this is a second string"
# # print(len(s1))
# # print(s1*3) 
# # for s in s1:
# #     print(s,end=" ")
# print(s2[0:4:2]) #euta space gardai slice gardai c

# string_input="I am learning python programming"
# if "learning" in string_input:
#     print("yes")
# else:
#     print("not")

# string_inputs="I am going to learn manchine learning"
# print("mach" in string_inputs)
# print("gl" in string_inputs)
# print("o le" in string_inputs)
# str3=string_inputs.split()
# print(str3)

# str5="Hello,how are you,where are you from?,by the way"
# print(str5.split(","))
# print(str5.strip("by"))


#list and tuple
# fruits=["orange","mango","banana","hheheheheh"]
# for fruit in fruits:
#     print("orange" in fruit)
# list1=[1,2,3,4,5,"python","ai"]
# print(type(list1))
# print(len(list1))
# for i in enumerate(list1): #enumerate is a function
#     print(i)
# list1.append("lekhee")
# print(list1)

# #To add the  element in the desired index
# list1.insert(0,"first")
# print(list1)
# #To remove the element
# list1.remove(1)
# print(list1)
        
# tuple1=(2,4,7,"manchine","learning")
# print(type(tuple1))
# for i in tuple1:
#     print(i)

# list1=[1,4,3,4,5,6,7,8]
# list2=[1,4,3,4,5,6,7,8]
# list1.remove(4)
# list1.pop(3)  #index bata remove garcha 3 index ko number remove garcha
# print(list1+list2)
# tuple1=(1,4,3,4,5,6,7,8)
# tuple2=(1,4,3,4,5,6,7,8)
# # list1.remove(4)
# # list1.pop(3)  #index bata remove garcha 3 index ko number remove garcha
# print(tuple1+tuple2)

# list_num=[2,3,4,5,6,7]  #list comprehension
# # list_square=[] #initalize
# list_square=[i**2 for i in list_num]  #This is shortcut method
# print(list_square)
# for i in list_num:
#     i=i**2
#     list_square.append(i)
# print(list_square)

#1 to 20 range ma even number finnd out
# num=[i for i in range(0,21) if i%2==0]
# print(num)

#dictionary in python 
# dict={"name":"sudip"}
# # print(type(dict))
# # print(dict)

# print(dict.keys())
# print(dict.values())

# dict1={
#     "name":"sudip",
#     "address":"itahari",
# }
# dict1["home"]=4
# print(dict1)

# for i in dict1.items():
#     print(i)

dict2={"subject":["python","java","c++","rust"], "marks":[67,54,65,89]} #dictionary bhitra list halni ni milxa
print(dict2)
for i in dict2.items():
    print(i)


