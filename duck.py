#!/usr/bin/env python
# encoding: utf-8

"""
@author: lvguangchao
@email: guangchao.lv@qq.com
@file: duck.py
@time: 2018/6/11 14:34
"""
class Duck(object):

    """ 策略模式

        守则一：变化的和不变化的分开
        继承可以帮助我们实现代码单一
        但是，对于不同类型子类，实现方式不同
        如果使用接口却过于重复，就可以抽象出来，由第三方类来实现

        守则二：面向接口编程，而不是面向实现编程
            如果使用适配器模式，就是一种面向实现编程

        守则三：多组合，少继承
    """

    def __init__(self):
        self.flyType=None

    def swim(self):
        print('i am swimg')

    def fly(self):
        self.flyType.fly()

    def set_fly_type(self,object):
        self.flyType=object

class FlyHandler(object):

    def fly(self):
        print('i am fly')

class FlyQuickHandler(object):

    def fly(self):
        print('i am quick fly')

if __name__ == '__main__':

    duck=Duck()
    duck.swim()
    duck.set_fly_type(FlyQuickHandler())
    duck.fly()