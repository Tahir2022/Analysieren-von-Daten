# a=2
# b=3
# alist_examp=[1,3.4,'asdf',96, True, 9.6,'zxcv',False, 2>5,a+b]
# print(alist_examp)
# print(type(alist_examp))
# print('This list contains ', len(alist_examp), ' elements')

# alist_examp=[1,3.4,'asdf',96, True, 9.6,'zxcv',False, 2>5,a+b]
# tmp=alist_examp
# print(tmp)
# print(alist_examp)
# tmp[3]='vbnm'
# print(tmp)
# print(alist_examp)

# tmp = alist_examp.copy()
# print(tmp)
# print(alist_examp)
# tmp[3]='vbnm'
# print(tmp)
# print(alist_examp)

# names = ['Jane', 'Margo', 'Sally']
# names.append('Sam')
# print(names)

# mylist = [1,2,4,5]
# mylist.pop(1)
# print(mylist)

# cheeses = ['Cheddar', 'Edam', 'Gouda']
# numbers = [42,135]
# empty = []
# print(cheeses, numbers, empty)
# print(cheeses[0])

# for cheese in cheeses:
#     print(cheese)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#     print(numbers)

# for i in []:
    # print('This never happens')

t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])

# t1 = ['a','b','c']
# t2 = ['d','e']
# t1.extend(t2)
# print(t1)

# def add_all(t):
#     total = 0
#     for x in t:
#         total +=x
#     return total

# s = 'spam'
# t = list(s)
# print(t)

# s = 'Please enter number'
# t = s.split()
# print(t)

# t = ['Please','enter','number']
# delimiter = ' '
# s = delimiter.join(t)
# print(s)

#Slicing

# x =[101, -45, 34, -300, 8, 9, -3, 22, 5]
#print()
#print(x)
#print(x[7:9])

# print()
# print(x[-1])
# print(x[-1:-3:-1])
# print(x[-1:-len(x)-1:-1])


#List methods

# list = ['larry', 'curly', 'moe']
# if 'curly' in list:
#     print('yay')

# strs = ['ccc', 'aaaa', 'd', 'bb']
# print(sorted(strs, key=len))
# print(sorted(strs, key=str.lower))

#Tuple

# nums = [1, 2, 3, 4]
# squares = [n * n for n in nums]
# print(squares)

# strs = ['hello', 'and', 'goodbye']
# shouting = [s.upper() + '!!!' for s in strs]
# print(shouting)

# nums = [2, 8, 1, 6]
# small = [n for n in nums if n <=2]
