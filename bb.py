#!/usr/bin/env python
# -*- coding:utf-8 -*-
from types import MethodType
from io import StringIO
from io import BytesIO
# class Student(object):
#     pass
#
# def set_age(self,age):
#     self.age=age

# s = Student()
# s.name = 'Michael'
# s.set_age=MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
# def set_score(self,score):
#     self.score=score
# Student.set_score=set_score
# s=Student()
# s.set_score(100)
# print(s.score)
# class Stduent(object):
#     __slots__ = ('name','age')
# def set_score(self,score):
#     self.age=score
# Stduent.set_score=set_score
# s=Stduent()
# s.name="zhangjpe"

# s.core=100
#

# class Student(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
# a=Student('zhang',200)
# print(a._Student__name)
# a._Student__name=200
# print(a._Student__name)

# class Students(object):
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer')
#         if value<0 or value>100:
#             raise ValueError('soore must betwwen 0 -100')
#         self.__score=value


# s = Students()
# s.score=26
# s.score
# print(s.score)
# class Student(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, name):
# 		self.name = name
# 	def __str__(self):
# 		return 'Student object(name: %s)' % self.name
# print(Student("zhang"))
# a,b,c=1,2,3
# print("%2d,%2d",a,b)
# a,b=b+2,a+b
# print("%2d,%2d",a,b,c)

# class Animal(object):
# 	def run(self):
# 		print('Animal is running')
# class Dog(Animal):
# 	pass

# dog=Dog()
# dog.run()

# print(type(dog))a
# try:
# 	f=open('C:\\Users\\zj\\Desktop\\python\\test.py','r')
# 	print(f.read())
# finally:
#     if f:
#         f.close()
# with open('C:\\Users\\zj\\Desktop\\python\\bb.py','rb') as f:
#     # for line in f.readlines():
#     #     print(line)
#     print(f.read())
# with open('C:\\Users\\zj\\Desktop\\python\\tt.txt','a') as g:
# 	g.write("hello,word\n")
# 	g.write("ljlkjkl\n")
#
#
# import pickle
# d = dict(name='Bob',age=20,score=88)
# print(d)
# print(pickle.dumps(d))
# print("hello")
