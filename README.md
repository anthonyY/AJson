# AJson

#### 一个json 和 对象互相转换的库，据我所知 demjson 好像只能转成dict 字典，不能转成写好的对象，就是当我们需要把json对应的对象直接保存到数据库时，
是还需要重新赋值的，所以我写了这么一个类。

### 使用方法  
#### 对象转json  
obj2Json(object, notFields)  
object 就是你的对象了， 比如我们要转成json时，去掉某个字段就可以传在第二个参数notFields，一个参数就用string, 如果是多个，就用list或者tuple
如：Student对象有 id, name, mobile, age, height, weight 字段， 我们不想要 身高体重信息,那么就这样协议
```
student = Student()
student.id = 1
'''其他字段省略'''
notFields = ["height", "weight"]
json = ajson.obj2Json(student, notFields)  
print(json)

```
以上内容就会得到以下内容，不会包含身高和体重。
```
{
    "id": 1,
    "name": "张三",
    "mobile": "13511112222",
    "age": 18
}
```

#### json 转 对象  
parseObj(obj, jsonStr)  
jsonStr就是json字符串， obj就是你要转换的对象。你可以提前把对象实例化传过来， 也可以传个类type过来，前提是这个type 是可以无参构造的。
如：
```
json = "{\"id\":1,\"name\":\"张三\",\"mobile\":\"13511112222\",\"age\":18}"
student = Student()
ajson.parseObj(student, json)  
print(student.name)

```
此时便会得到 “张三”。  
  
由于python 语言是动态类型的，所以list和tuple 里面的对象类型是无法识别的，所以统统自动转成了string, 好吧，我也很为难。但是我想了个特别的方法，
从理论上来说是不合理的，但是结果是可行的，就是初始化是 list 默认给一个item, 而item的内容则是给类型的type,比如:
```
students=[Student]
```
这样就可以解析了，但是如果你没有做json的转换就去调用它，你就会得到一个有一个item的列表，并不合理，所以要这样做的话，必须考虑好，谨慎使用。  

