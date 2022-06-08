def fact(x):
  return 1 if (x < 1) else x*fact(x-1)

def filter_even(li):
  return list(filter(lambda x: x % 2 == 0,li))

def square(li):
  return list(map(lambda x: x**2,li))

def bin_search(li, element): 
    first = 0 
    last = len(li)-1 
    i = -1 
    while (first<=last) and (i==-1):
        mid = (first+last)//2
        if li[mid] == element:
            i=mid
        else:
            if element<li[mid]:
                last=mid-1
            else:
                first=mid+1
    return i

def is_palindrome(string):
    string = ''.join(filter(str.isalpha, string)).lower()
    i = 0
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

import re
import json

def decode_ch(sting_of_elements):
    result=""
    with open('periodic_table.json', 'r', encoding='utf-8') as f:
        periodic_table = json.load(f)
        f.close()
    list_of_elements = re.findall('[A-Z][a-z]*', sting_of_elements)
    for e in list_of_elements:
        result+=periodic_table.get(e)
    return result

class Student:
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
        self.__msg = msg
        
        super(MyError, self).__init__(msg)
        
    def __str__(self):
        return self.__msg
    
    def get_msg(self):
        return self.__msg
