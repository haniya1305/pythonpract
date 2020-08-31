import re

# string1 = "hi i am haniya"
# result = re.search("am", string1)
# print(result)

#Email ID
def emid():
    email = "haniya_1305@gmail.com"
    result1 = re.search(r'^[a-z0-9]+[._]{0,1}[a-z0-9]+@[a-z]+.com', email)
    print(result1)

    # email_id = "haniya.nizar.ahamed.mohammed.amir@gmail.com  nithya__@gmail.com"
    # result2 = re.findall(r'^[a-z0-9]+[._a-z0-9]+@[a-z]+.com', email_id)
    # print(result2)

#Phone Number
def phn():
    phone_no = "00971502517740 00919739426248"
    check = re.search(r'^0097150+[0-9]{7}', phone_no)
    print(check)

    # phone = "00971502443636 00971502517740 00919739426248"
    # check1=re.findall(r'^009715+[0-9]{8}',phone)
    # print(check1)
    #
    # p_no="00971502517740 00919739426248 00971562443636"
    # check2=re.findall(r'^009715+[056]{1}[0-9]{7}',p_no)
    # print(check2)


#IP Address
def ipad():
    ip_add = "192.74.22.24 19.35.74.3 "
    r = re.search(r'\d{3}.\d{1,3}.\d{1,3}.\d{1,3}', ip_add)
    print(r)

    # ipadd = "192.74.22.24 19.35.74.3 103.4.63.6"
    # r1 = re.findall(r'\d{3}.\d{1,3}.\d{1,3}.\d{1,3}', ipadd)
    # print(r1)

#Credit Card
def CredC():
    nstr = "4444456798263192"
    res = re.search(r'[0-9]{16}', nstr)
    print(res)

    # newstr = "4444456798263192 1234729046 0938147284926470"
    # res2 = re.findall(r'[0-9]{16}', newstr)
    # print(res2)

print("Choose an option: 1)Email Address 2)Phone Number 3)IP Address 4)Credit Card ")
choice = int(input("Enter a choice between 1 and 4 : "))

if choice == 1:
    emid()
elif choice == 2:
    phn()
elif choice == 3:
    ipad()
elif choice == 4:
    CredC()
else:
    print("Wrong Choice!")