#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

"""
判断obj对象是否继承至cls
"""
def ischildof(obj, cls):
    try:
        for i in obj.__bases__:
            if i is cls or isinstance(i, cls):
                return True
        for i in obj.__bases__:
            if ischildof(i, cls):
                return True
    except AttributeError:
        return ischildof(obj.__class__, cls)
    return False

"""
检查字段是否需要过滤
"""
def checkNoField(key, notFields):
    filter = False
    if notFields != None:
        type1 = type(notFields)
        if type1 == list or type1 == tuple :
            for notField in notFields:
                if key == notField:
                    filter = True
                    break
        elif type1 == str:
            # 不需要组装json的就过滤掉
            filter = (key == notFields)
    return filter
"""
对象转成json字符串
obj 对象
notFields 不需要的字段 如果只过滤一个可以传字符串，否则传列表list或者 元组tuple
"""
def obj2Json(obj, notFields=None):
    if(obj == None):
        return None
    if(isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, bool)) :
        return str(obj)
    if(isinstance(obj, dict)) :
        return json.dumps(obj)
    if(isinstance(obj, type)) :
        return str(obj)
    result = "{"

    for key, value in vars(obj).items():
        if value == None:
            continue
        # 这个字段是否是不组包的字段
        isNotField = checkNoField(key, notFields)

        # 不需要组装json的就过滤掉
        if isNotField:
            continue
        result+="\""+key+"\":"
        fieldType = type(obj.__getattribute__(key))
        if fieldType is tuple or fieldType is list:
            result += "["
            for item in value:
                if isinstance(item, int) == int or isinstance(item, float):
                    result += str(item)+","
                elif isinstance(item, str):
                    result += "\""+str(item)+"\","
                else :
                    result += obj2Json(item, notFields)+","
            if result[-1] == ',':
                # 最后一个是,就删除这个,
                result = result[:-1]
            result += "],"
        elif fieldType is type(str) :
            result += "\""+str(value)+"\","
        else :
            result += obj2Json(value)+","



    if result[-1] == ',':
        # 最后一个是,就删除这个,
        result = result[:-1]
    result +="}"
    return result



"""
把json解析成对象
"""
def parseObj(obj, jsonStr):
    if(type(obj) == type(type)):
        obj = obj()
    print(str(type(obj)))
    jsonDict = json.loads(jsonStr)
    objDict = obj.__class__.__dict__.items()
    for key, value in jsonDict.items():
        if(key[0:2] == "__"):
            continue
        for key2, value2 in objDict:
            if(key2[0:2] == "__"):
                continue

            if key == key2:
                fieldType = type(obj.__getattribute__(key))

                if fieldType == int:
                    value3 = int(value)
                elif fieldType == float:
                    value3 = float(value)
                elif fieldType == bool:
                    value3 = bool(value)
                elif fieldType == str:
                    value3 = str(value)
                elif fieldType == dict:
                    value3 = dict(value)
                elif fieldType == tuple:
                    lenth = len(value)
                    temp = []
                    for i in range(lenth):
                        if(len(value2) > 0 and type(value2[0]) == type):
                            pass
                            value3.append(parseListChild(value[i], value2[0]))
                        else:
                            value3.append(parseListChild(value[i]))
                    value3 = tuple(temp)

                elif fieldType == list:
                    lenth = len(value)
                    value3 = []
                    for i in range(lenth):
                        if(len(value2) > 0 and type(value2[0]) == type):
                            pass
                            value3.append(parseListChild(value[i], value2[0]))
                        else:
                            value3.append(parseListChild(value[i]))

                elif ischildof(value2, fieldType):
                    tempClass = getattr(obj, key)
                    newClass = tempClass()
                    #valus 是字典，转成str也是单引号的，所以还是要用json.dumps转成双引号格式的字符串
                    jsonChildStr = json.dumps(value)
                    value3 = parseObj(newClass, jsonChildStr)

                else :
                    tempClass = getattr(obj, key)
                    newClass = tempClass()
                    #valus 是字典，转成str也是单引号的，所以还是要用json.dumps转成双引号格式的字符串
                    jsonChildStr = json.dumps(value)
                    value3 = parseObj(newClass, jsonChildStr)

                setattr(obj, key, value3)
                # try:
                #
                # except Exception as err:
                #     print("parse json error field "+key+" "+str(value), err)
    return obj

"""
处理list里面的内容，再返回给list
"""
def parseListChild(obj, newClass=None):
    #{开头说明是对象
    if str(obj)[0] == '{':
        #valus 是字典，转成str也是单引号的，所以还是要用json.dumps转成双引号格式的字符串
        jsonChildStr = json.dumps(obj)
        if newClass == None or newClass == type:
            pass
            return jsonChildStr
        else:
            newValue = parseObj(newClass(), jsonChildStr)
            return newValue
    #TODO 此时并不知道list里的类型，所以没法弄成自己想要的对象，那暂时只能先用string接收喽
    # 此处我加了处理，就是定义变量时先给他一个有一个item的值，里面的类型就是你定义的类型，list[Student]，然后就可以解析了，但是这个其实并不合理，就啊开始时你的列表就有一个item了，很容易让你误解

    else :
        return obj


