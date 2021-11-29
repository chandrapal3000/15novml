#03
s1 = "Nice to have it"
s2 = "here"
print(s1 + " " + s2)

#04
a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#05
a.insert(0, s1)
a.append(s2)
print(a)

#06
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        print(i)
        break

#07
color_list1 = set(["White", "Black", "Red"])
color_list2 = set(["Red", "Green"])
print(color_list1.difference(color_list2))

#08
user = input("Enter string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
flag = 0
user.lower()

for x in alphabet:
    if x in user:
        flag += 1

if flag>=26:
    print("a pangram")
else:
    print("not a pangram")

#09
user = eval(input("Enter a no.: "))
print(user+user*11+user*111)

#10
user = input("Enter no.: ")
user = user.split('#')
first = user[0].split(" ")
second = user[1].split(" ")

for x in range(len(first)):
    first[x] = eval(first[x])
for x in range(len(second)):
    second[x] = eval(second[x])

print(first)
print(second)

#11
user = input("Enter input number: ")
user = user.split(',')
print(sorted(user))

#12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
flag = -1
new = sorted(d['Marks'], reverse=True)

for x in d['Marks']:
    flag += 1
    if x==new[0]:
        break
print(d['Student'][flag])

#13
userin = input('Enter a sentence: ')
LETTERS = 0
NUM = 0
for x in userin:
    if x.isalpha():
        LETTERS += 1
    if x.isnumeric():
        NUM += 1
print("LETTERS",LETTERS)
print("NUM",NUM)

#14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

userin = input("Enter subject : ")
new = {'Name':[], 'Subject':[], 'Ratings':[]}

for x in range(len(d['Name'])):
    if d['Subject'][x]==userin:
        new['Name'].append(d['Name'][x])
        new['Subject'].append(d['Subject'][x])
        new['Ratings'].append(d['Ratings'][x])
print(new)