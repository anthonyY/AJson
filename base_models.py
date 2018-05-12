# -*- coding: utf-8 -*-
#!/usr/bin/python

class Entity:
    pass
    # def toString(self):
    #     return obj2Json(self)

class Student(Entity) :
    id = 0
    name = ""
    age = 0
    mobile = ""
    imageIds = ()
    ids = []
    names = []


class Teacher(Entity):
    id = 0
    name = ""
    age = 0
    student = Student
    #students = [Student] 这样写就会解析的很好，但是一开始students就有一个Student的元素了
    #students = [] 这样解析出来的结果就是字符串类型的list,而不能当成指定类型使用
    students = [Student]

class Strr(Entity):
    attrs = {}