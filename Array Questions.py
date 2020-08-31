#Question 1
list1 = [1,1,1,2,2,3,3,3,3,5,5,5,5,5,7,7,7,7,7]
number = int(input())
newlist= []

set1= set(list1)
list=list(set1)
print(list)

for i in range(0,number):
    m=max(list)
    newlist.append(m)
    list.pop()

print(newlist)

#Question 2
string1= "the panda is crazy"
found = False

for i in range(0, len(string1)-1):
    for j in range(i+1, len(string1)-1):
        if string1[i] == string1[j] and string1[i]!=" ":
            print(string1[j])
            found = True
            break
    if (found):
        break

#Question 3
nlist=[1,2,3,4,6,7,8,9,10]
for i in range(0,len(nlist)-1):
    if (nlist[i+1]-nlist[i]==2):
        print(nlist[i]+1)

# another method

newlist=[1,5,2,4]
newlist.sort()
start=newlist[0]
end=newlist[-1]
print(newlist)
sum1 = 0
sum2 = 0

for i in newlist:
    sum1 = i + sum1
print(sum1)

for i in range(start,end+1):
    sum2 =  sum2 + i
print(sum2)

x= sum2-sum1
print("Missing Element: ")
print(x)
