#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
测试 对象组成json
"""
import unittest
import ajson
from base_models import Teacher, Student

class TestMathFunc(unittest.TestCase):

    def testObj2Json(self):
        teacher = Teacher()
        student = Student()
        student.id = 1
        student.name = "zhangsan"
        student.age = 18
        student.ids = (5,6,8,1)
        student.imageIds = [1,6,3,4]
        student.names = [">>","errrr","MMM","saas"]

        student2 = Student()
        student2.id = 12
        student2.name = "lisi"
        student2.age = 11
        student2.ids = (6,8,0)
        students = []
        students.append(student)
        students.append(student2)


        teacher.name = "张老师"
        teacher.id = 99
        teacher.age = 43
        teacher.student = student
        teacher.students = students
        # json = obj2Json(student, "name")
        # notFields = ["name", "id"]
        # notFields = ("name", "id")
        # json = obj2Json(student, notFields)

        json = ajson.obj2Json(teacher)
        print(json)

    """
    测试json转成对象，
    存在的一个问题就是list装对象时，无法解析成对应的对象，只能弄成string,请使用者把list的内容当做string自行处理
    """
    def testJsonToObj(self):
        # jsonStr = "{\"id\":\"1\",\"name\":\"zhangsan\",\"age\":18}"
        jsonStr = "{\"name\":\"张老师\",\"id\":\"99\",\"age\":\"43\",\"student\":{\"id\":\"1\",\"name\":\"nngf\",\"age\":\"18\",\"ids\":[5,6,8,1],\"imageIds\":[1,6,3,4]},\"students\":[{\"id\":\"1\",\"name\":\"saas\",\"age\":\"18\",\"ids\":[5,6,8,1],\"imageIds\":[1,6,3,4]},{\"id\":\"12\",\"name\":\"lisi\",\"age\":\"11\",\"ids\":[6,8,0]}]}"
        teacher = Teacher()
        ajson.parseObj(teacher, jsonStr)
        print("=======name="+teacher.name)
        print("======student =name="+str(teacher.student))
        #此处无法获取list子类型，所以list里只能装string 等常用数据类型
        print("======student[0] type="+str(type(teacher.students[0])))
        print("======student[0] = "+ajson.obj2Json(teacher.students[0]))
        print("======student[0].name = "+teacher.students[0].name)

    if __name__ == '__main__':
        unittest.main()
        # testJsonToObj()
        # tObj2Json()

    # jsonStr = "{\"id\":\"1\",\"name\":\"zhangsan\",\"age\":\"18\",\"ids\":[5,6,8,1],\"imageIds\":[1,6,3,4],\"names\":[\">>\",\"errrr\",\"MMM\",\"saas\"]}"
    # teacher = Teacher()
    # tempClass = getattr(teacher, "student")
    # newClass = tempClass()
    # parseObj(newClass, jsonStr)
    # # print(">>>>>>>"+str(newClass))
    # print( "student name = "+getattr(newClass, "name"))
    # fieldType = type(teacher.__getattribute__("students"))
    # print(fieldType)
    # print(type(Student) == type)