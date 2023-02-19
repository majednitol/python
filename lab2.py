

# number =int (input ("Enter number"))


# if number >= 80:
#     print("A+")

# elif 70 <= number and number <= 79:
#     print("A")


# elif 60 <= number and number<= 69:
#     print("A-")


# elif 50 <= number and number<= 59:
#     print("B")

# elif   40<=number and number<=49 :
#     print("C")
# else:
#     print("fail")


# fr = ["apple", "mango", "orange"]

# for item in fr:
#     print(item)


# for num in range(60):
#  print(num)


# for str in "mango apple":
#     print(str)


# colour = ["red", "blue", "green"]

# for item in colour:

#     if item == "blue":
#         # break
#         # continue
#         pass

#     print(item)


# for i in range(10, 0, -1):
#     print(i, end=" ")


# i = 1
# while (i < 10):
#     print(i)
#     i = i+1


# age = int(input("enter age"))
# if age>18:
#     print("person is eligible for voting")

# else :
#     print("person is eligible for voting")

# year = int(input("enter a year "))
# if year % 4 == 0:
#     print("this year is leap year")
# else:
#     print("this year is not leap year")

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print("A is greater")
# elif b > a and b > c:
#     print("B is greater")
# else:
#     print("C is greter")


# sum = 0
# i = 1
# for i in range(50):
#     sum = sum+i
# print(sum)


n = int(input())
a =0 
while n!=0 :
    rem = n%10
    a = a * 10 + rem
    n= n//10
    
print(a)