"""
author jiqiang
观察者模式
updated_time 2019.6.25
"""


class Observerable:
    # 被观察者基类

    def __init__(self):
        self.__observer = []

    def add_observer(self, observer):
        self.__observer.append(observer)

    def remove_observer(self, observer):
        self.__observer.remove(observer)

    def notify_observers(self, observer_able):
        for o in self.__observer:
            o.notify(observer_able)


class HeatWater(Observerable):
    # 热水器，冬天的神器

    def __init__(self):
        self.__temperature = 0
        super().__init__()

    # 获取温度
    def get_temperature(self):
        return self.__temperature

    # 获取温度
    def set_temperature(self, temperature):
        if temperature > 100:
            raise ValueError('参数错误！')
        self.__temperature = temperature
        print('Current temperature is ', self.__temperature)
        self.notify_observers(self)


class Observer:

    # 观察者基类 通知方法
    def notify(self):
        pass


class DrinkingMood(Observer):

    # 喝水模式
    def notify(self, observe_object):
        if isinstance(observe_object, HeatWater) and observe_object.get_temperature() >= 100:
            print("可以喝水了！")


class WashingMood(Observer):

    # 洗澡模式
    def notify(self, observe_object):
        if isinstance(observe_object, HeatWater) and observe_object.get_temperature() > 70:
            print('可以洗澡了！')


class TestClass:

    # 测试类
    def __init__(self, t):
        thing = HeatWater()
        water = DrinkingMood()
        shower = WashingMood()

        thing.add_observer(water)
        thing.add_observer(shower)

        thing.set_temperature(t)


while 1:

    try:
        a = input()
        a = int(a)
        TestClass(a)

    except ValueError:
        break

