import re

# Problem 1
string1 = 'aabbbccdxxxxx'
count = 0

while (len(string1)>0):
    count = 1
    temp = ''

    for i in range(1,len(string1)):
        if string1[0] == string1[i]:
            count = count + 1
        else:
            temp = temp + string1[i]
    print(string1[0], count)
    string1 = temp

# Problem 2
list1=[1,2,3,6,4,2]
list1=[1,2,3,1,6]


for i in range(0,len(list1)-1):

    lsum = 0
    j = i - 1
    while (j>=0):
        lsum = lsum + list1[j]
        j = j - 1

    rsum = 0
    k = i + 1
    while (k < len(list1)):
        rsum = rsum +list1[k]
        k = k + 1

    if (lsum == rsum):
        print(list1[i])

# Problem 3
# Validate user: ‘username_123’
# 1.Len of usernme shld be 8 or more
# 2.Name shld start with alpha
# 3.Only _ special character is allowed.

user = 'username_123'
result1 = re.match(r'^[a-z]{1}[_\w]{7}[_\w]*', user)
print(result1)

if (re.match(r'^[a-z]{1}[_\w]{7}[_\w]?', user)):
    print("Valid")
else:
    print("Not Valid")