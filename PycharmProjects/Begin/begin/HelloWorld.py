
print("Hello Python")
fruits = ['apple', 'banana', 'mango']

for fruit in fruits:
    print('current fruit: ', fruit)

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1


def plus(a, b):
    return a + b


print("call function sum: ", plus(1, 2))

hello = 'Hello World'

print(hello[0:4])
print(hello[6:-3])
print(hello[:4])
print(hello[-3:])
count = len(hello)
hello2 = hello.replace('World', 'Python')
print(hello2)
print(hello.find('Python'))
print(hello2.find('Python'))
print(hello.split(' '))
#List
numbers = [1, 2, 3, 4, 5]
print(numbers[3])
print("index for 4: ", numbers.index(4))
del numbers[2]
print(numbers)
numbers.append(8)
print(numbers)
myNumber: int = numbers.pop()
print(myNumber)
print(numbers)
numbers.reverse()
print(numbers)
aList = ['edf', 'asd', 'axa', 'gx']
print(sorted(aList))
#Tuple
myTuple = ('x', 'y', 'z')
print(myTuple)
#Dictionary (gồm key and value)
point = {'x': 1, 'y': 3, 'z': 8}
print(point['x'])
user = {'name': 'Huy', 'age': 20, 'country': 'Viet Nam'}
print(user)
#dict.clear(): xoa toan bo du lieu trong doi tuong
#dict.copy(): tra va 1 ban copy cua doi tuong
#dict.fromkeys(seq[, value]): tao mot doi tuong voi danh sach key tu seq va neu co truyen value thi lay do lam gia tri cho ca phan tu
#dict.has_key(key): kiem tra 1 key co ton tai k
#dict.keys(); tra ve 1 list chua ca key
#dict.values: tra ve 1 list chua cac value
