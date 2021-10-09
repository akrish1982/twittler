# #FUndction explained here with all types
#
# # def msg():
# #     print("Hello")
# # msg()
# #
# # def ms(a,b):
# #     print(a + b)
# # ms(10,20)
# #
# # def ms(a,b):
# #      sum = a + b
# # a = ms(10,20)
# # print(a)
# #
# # def ms(a,b):
# #      sum = a + b
# #      sub = b - a
# #      return sum,sub
# # a,b = ms(1,2)
# # print(a,",",b)
# #
# # # print(b)
# #
# # def ed(name,age):
# #     print("employee name is", name,"emplo age is",age)
# #     # return ("employee name is", name,"emplo age is",age)
# # # x = ed(age=25,name='str')
# # # print(x)
# # ed(age=25,name='str')
# #
# # def ed(name,age=35):
# #     print("employee name is", name," & emplo age is",age)
# #     # return ("employee name is", name,"emplo age is",age)
# # # x = ed(age=25,name='str')
# # # print(x)
# # ed(age=40,name='str')
# #
# # def vl(*name):
# #     return name
# # a,b,c,d= vl("sunthar","surya","ammu","anbey")
# # print(a)
# #
# #
# # def vlka(**details):
# #     print(details)
# #     return details
# #
# # k = vlka(id=123,name="bala",phone= 8146815668)
# # s = k.items()
# # print(s)#
# #functions
# #2
# # a = 1
# # def get_res():
# #     a = 2
# #     print("inside",a)
# # get_res()
# #
# #
# # a = 1
# # def get_res(a):
# #     a = 2
# #     print("passed as parameter and mentioned inside",a)
# # get_res(3)
# #
# #
# # a = 1
# # def get_res(a):
# #     print("passed as parameter, not inside only outside",a)
# # get_res(3)
# #
# #
# #
# # a = 1
# # def get_res():
# #     print("mentioned oustide only",a)
# # get_res()
# #
# # b = 1
# # def get_res():
# #     global b
# #     # b = 150
# #     print("Given global",b)
# # get_res()
# #
# #
# # b = 100
# # def get_res():
# #     b = 2
# #     x=globals()['b']
# #     print(" inside ",x)
# #     print(globals()['b'])
# #     y = globals()['b']= 24
# #     # y = globals()['b']
# #     print(y,"y")
# # get_res()
# # print(b,"hellooo")
#
# #global and Local Variable
#
# # def f():
# #     x = 100
# #     print(x)
# # f()
# # print(x)
# #
# # print(dir())
# # x = 1
# # print(dir())
#
# # print("1: Decorators")
# # def upper(func):
# #     def inner():
# #         str1 = func()
# #         return str1.upper()
# #     return inner()
# # @upper
# # def good():
# #     return "good Morning Da"
# # print(good)
# # # d= upper(good)
# # # print(d())
# # print()
# # #
# # # # print("2: Decorators with returning")
# #
# # a = 1_2_3
# # print(a/2)
#
#
# # 🚨 Don't change the code below 👇
# age = int(input("What is your current age?"))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# daylife = 90*365
# days = daylife - (age * 365)
#
# weeklife = daylife / 7
# weeks = (weeklife-(days/7))
#
# # m=((90*365)/12)
# # months = (mon_exp- (days//12)
#
# print()
# print(f"You have {days} days, {weeks} weeks")

# print(round(3.2111,2))

def a(a,b):
    return a+b
c=a(10,20)
# print(c)