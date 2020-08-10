# DAY 2 HW
# string= "  This is the string  "
# print(string)
# string.strip()
# print(string)
#
# list1= string.split(' ')
# print(string)
# print(list1)
#
# print("\nAfter reversing each word in itself:")
# for i in range (0, len(list1)):
#    list1[i] = list1[i][::-1]
# string1=" ".join(list1)
#
# print(list1)
# print(string1)
#
# DAY 3 HW
# problem 1
# string1="abcedf"
# print(string1)
# print('Converting into list-')
# string_list=list(string1)
# print(string_list)
# print('Removing element-')
# string_list.remove('d')
# print(string_list)
#
# problem 2
# list1= ['abc','name','someothername','chooseurname','dntchangeurname','ab','a']
# for i in range (0,len(list1)):
#     if len(list1[i])>=3:
#         string=list1[i]
#         print(string.upper())
#     else:
#         print(list1[i])

# list1= ['abc','name','someothername','chooseurname','dntchangeurname','ab','a']
# new_list=[print(str(i).upper()) for i in list1]
# new_list=[print(str(list1[i]).upper()) for i in range(0,len(list1))]

# problem 3
# string1='this is string'
# temp=''
# print(string1)
# print('after reversing...')
# for i in string1:
#     temp = i + temp
# print(temp)
#
#
# problem 4
# List1=[1,2,3,10,11,1001,120]
# for i in range(0,len(List1)):
#     if List1[i]%2 == 0 and i%2 == 0:
#         print("The value and index are divisible by 2")
#     else:
#         print("The value and index are not divisible by 2")
#
# DAY 4 HW
# string='this is string'
# leng=len(string)
# for i in range(0,leng):
#      count=0
#      temp=string[i]
#      for j in range(0,leng):
#          if string[j]==temp:
#              count+=1
#      print('the number of times the character',string[i],'is',count)
#
#
# DAY 6 HW
# problem 1
# List=['a','b','c','d','a','b','c','xyz','xyz']
# leng=len(List)
# for i in range(0,leng):
#      count=0
#      temp=List[i]
#      for j in range(0,leng):
#          if List[j]==temp:
#              count+=1
#      print('the number of times the character',List[i],'is',count)
#
# problem 2
# List=[('a','b'),('c','d'),(1,2),(4,5)]
# dict1=dict(List)
# print(dict1)
#
# problem 3
# List1=[1,2,3,4,5,6]
# List2=[10,20,30,40,50]
# j = 1
# for i in List2:
#     List1.insert(j, i)
#     j += 2
# print(List1)
#
# problem 4
# List1=[1,2,3,4,4,5,6,78,11]
# List2=[10,1,2,50,100]
# set1=set(List1)
# set2=set(List2)
# temp=set1.intersection(set2)
# print(temp)
# print("Printing squares of elements....")
# for i in temp:
#     print(i*i)

#DAY 7 HW

#list input
# list=input().split(' ')
# print(list)

#tuple input
# tupl=input().split(',')
# tup=tuple(tupl)
# print(tup)

#DAY 7 HW

#dict input
# l1=[]
# l2=[]
# list1=input().split(' ')
# for i in range(0,len(list1),2):
#     l1.append(list1[i])
#     l2.append(list1[i+1])
# list1=zip(l1,l2)
# dict1=dict(list1)
# print(dict1)

#dict comprehension
# names=['haniya',"ma'am"]
# roles=['student','teacher']
# role_dict={name:role for name,role in zip(names,roles) if name=='haniya'}
# print(role_dict)

#set comprehension
# set1={1,2,3,4,5,6}
# temp_set= {value for value in set1 if value%2==0}
# print(set1)
# print(temp_set)

# list1=[1,2,3,4]
# list2=[10,20,30,40]
# zipline=zip(list1,list2)
# print(zipline)