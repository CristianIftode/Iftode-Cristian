
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)
    pass

print (fact(10))


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  return 1 if (x < 1) else x*fact(x-1)

def filter_even(li):
    a = list(filter(lambda x: x % 2 == 0, li))
    return a
    pass

print(filter_even(li))

L = [1, 2, 3, 4]
  return list(filter(lambda x: x % 2 == 0,li))

def square(li):
    a = list(map(lambda x: x**2, li))
    return a
    pass

print (square(L))

li = [2, 5, 7, 9, 11, 17, 222]
element = 11


def bin_search(li, element):
    first = 0
    last = len(li) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
  return list(map(lambda x: x**2,li))

def bin_search(li, element): 
    first = 0 
    last = len(li)-1 
    i = -1 
    while (first<=last) and (i==-1):
        mid = (first+last)//2
        if li[mid] == element:
            index = mid
            i=mid
        else:
            if element < li[mid]:
                last = mid - 1
            if element<li[mid]:
                last=mid-1
            else:
                first = mid + 1
    return index


print(bin_search(li, element))

import re

st = input("Введите слово: ")
nst = re.sub(r'[^\w\s]','', st)
nnst = nst.replace(" ", "")
                first=mid+1
    return i

def is_palindrome(string):
    letters = list(string)
    palin = True
    string = ''.join(filter(str.isalpha, string)).lower()
    i = 0
    while len(letters) > 0 and palin:
        if letters[0] != letters[(len(letters) - 1)]:
            palin = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))
    return palin
if is_palindrome(nnst.lower()):
    print ("YES")
else:
    print("No")



lst = []
    j = len(string)-1
    pal = True
    while (i<j) and pal:
        if(string[i]!=string[j]):
            pal = False
        i += 1
        j -= 1
    return pal
operations = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '%': lambda x, y: x % y,
    '//': lambda x, y: x // y,
    '**': lambda x, y: x ** y,
}

def resolve(op, a, b): 
    return operations[op](a, b) 

def calculate(path2file):
    result="" 
    with open(path2file, mode='r') as f:
        while(True):
            line = f.readline()
            if not line:
                break
            op=line.split()[0]
            a =int(line.split()[1])
            b =int(line.split()[2])
            if result=="":
                result=str(resolve(op,a,b))
            else:
                result=result+","+str(resolve(op,a,b))
        f.close()
    return result

def substring_slice(path2file_1,path2file_2):
    result=""
    with open(path2file_1, mode='r') as f1:
        with open(path2file_2,mode='r') as f2:
            while(True):
                line1 = f1.readline()
                line2 = f2.readline()
                if not line1 or not line2:
                    break
                i=int(line2.split()[0])
                j=int(line2.split()[1])
                if result=="":
                    result=line1[i:j+1] 
                else:
                    result=result+" "+line1[i:j+1]
            f1.close()
        f2.close()
    return result

    return int(eval(f'{int(path2file[1])}{path2file[0]}{int(path2file[2])}'))

with open('test_input_file_1.txt', 'r') as FILE:
    for row in FILE:

        lst_1 = row.split()
        lst.append(calculate(lst_1))

with open('test_output_file_1.txt', 'w') as FILE:
    for i in range(len(lst)):
        if i != len(lst) - 1:
            FILE.write(str(lst[i]) + ', ')
        else:
            FILE.write(str(lst[i]))



lst = []


def substring_slice(path2file_1, path2file_2):

    a = int(path2file_2[0])
    b = list(str(path2file_1[0]))
    l = []
    while a <= int(path2file_2[1]):
        l.append(str(b[a]))
        a = a + 1
    return l

with open('test_import_file_2_1.txt', 'r') as FILE1, open('test_import_file_2_2.txt', 'r') as FILE2:
    for row in FILE1:
        lst_1 = row.split()
        lst_2 = FILE2.readline().split()
        lst.append(str(''.join(substring_slice(lst_1, lst_2))))

with open('test_output_file_2.txt', 'w') as FILE:
    for i in range(len(lst)):
        if i != len(lst) - 1:
            FILE.write(str(lst[i]) + ' ')
        else:
            FILE.write(str(lst[i]))



import re
import json
a = "NOTiFICaTiON"

with open('periodic_table.json', encoding='utf-8') as f:
     d = json.load(f)


def decode_ch(sting_of_elements):
    lst = list(sting_of_elements)
    l = []
    i = 0
    while i < len(lst):
        if i < len(lst) - 1:
            if lst[i].isupper() and lst[i + 1].isupper():
                l.append(lst[i])
                i = i + 1

            else:
                l.append(lst[i] + lst[i + 1])
                i = i + 2
        else:
            l.append(lst[i])
            i = i + 1
    st = ""
    for i in range(len(l)):
        st = st + d[l[i]]
    return st
    pass



print(decode_ch(a))



from statistics import mean
    result=""
    with open('periodic_table.json', 'r', encoding='utf-8') as f:
        periodic_table = json.load(f)
        f.close()
    list_of_elements = re.findall('[A-Z][a-z]*', sting_of_elements)
    for e in list_of_elements:
        result+=periodic_table.get(e)
    return result

class Student:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.grades = []
    self.fullname = name + " " + surname
  def grades(self):
    print ("Hello, I am Student")
  def mean_grade(self):
    m = mean(self.grades)
    return m
  def is_otlichnik(self):
    m = mean(self.grades)
    if m >= 4.5:
      print("YES")
    else:
      print("NO")
  def __add__(self, otherName):
    return self.name + " is friends with " + otherName.name
  def __str__(self):
    return "{}".format(self.fullname)
  pass

newstud = Student('OLeg', 'Olegov')
newstud_2 = Student('Ivan', 'Ivanov')
newstud.grades = [4,5,5,5]
newstud.is_otlichnik()

print(newstud + newstud_2)

print(newstud)
    def __init__(self, name, surname, grades=[3,4,5]):
        self.__name = name
        self.__surname = surname
        self.__fullname = name + ' ' + surname
        self.__grades = grades

    def greeting(self):
        return ("Hello, I am Student")

    def mean_grade(self):
        return sum(self.__grades)/len(self.__grades)

    def is_otlichnik(self):
        if self.mean_grade()>=4.5:
            return "YES"
        else:
            return "NO"
    #magic
    def __add__(self, other):
        return (self.__name + " is friends with " + other.__name)

    def __str__(self):
        return self.__fullname

class MyError(Exception):

    def __init__(self, msg):
        if msg:
            self.message = msg[0]
        else:
            self.message = None

        self.__msg = msg

        super(MyError, self).__init__(msg)

    def __str__(self):
        print('Вызов ошибки')
        return 'Мой класс исключений, {0} '.format(self.message)

err = MyError('У нас ошибка')

raise(err)
        return self.__msg

    def get_msg(self):
        return self.__msg
