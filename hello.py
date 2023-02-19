# age1 = input("what is your age ")
# age2 = input("what is your age ")
# newAge = int(age1) +int(age2)
# print(newAge)

name = 'majedur rahman'
print(name.upper())
print(name.lower())
print(name.find('m'))
print(name.replace('majedur', 'nitol'))
print(name.lower())
# find string or character
print('r' in name)
# power **
print(5**2)

print(2 > 5 or 8 < 9)
print(2 > 5 and 8 < 9)
print(not 7 > 8)
age = 60
if age > 18:
    print('you are adult')
elif age < 17:
    print('you are school')
else:
    print('you are child')
print(range(5))

i = 1
while i <= 5:
    print(i * "*")
    i = i + 1


for item in range(5):
    print(item + 1)


marks = [90, 80, 79]
marks.append(80)
marks.insert(0, 89)

for item in marks:
    print(item)
    print(len(marks))


i = 0
while i < len(marks):
    print(marks[i])
    i= i +1


marks.sort()
marks.clear()
print(marks)



mark = {'english':80, 'chemistry' :90}
mark ['ban'] = 56
print(mark)
mark ['ban'] = 560
print(mark)
