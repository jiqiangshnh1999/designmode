"""
author jiqiang
观察者模式
updated_time 2019.6.25
"""


class Subject:

    def __init__(self):
        self.__observer = []

    def addObserver(self, observer):
        self.__observer.append(observer)

    def removeObserver(self, observer):
        self.__observer.remove(observer)

    def getObserver(self):
        return self.__observer


class HeatWater(Subject):

    def __init__(self):
        self.__temperature = 0
        super().__init__()

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        self.notify()

    def notify(self):
        for o in self.getObserver():
            o.update(self.__temperature)


class Observer:

    def __init__(self):
        pass


class WaterMood(Observer):

    def update(self, temperature):
        if temperature >= 100:
            print("可以喝水了！")


class ShowerMood(Observer):

    def update(self, temperature):
        if temperature > 70:
            print('可以洗澡了！')


class TestClass:

    def __init__(self, t):
        thing = HeatWater()
        water = WaterMood()
        shower = ShowerMood()

        thing.addObserver(water)
        thing.addObserver(shower)

        thing.setTemperature(t)


while 1:

    try:
        a = input()
        a = int(a)
        TestClass(a)

    except Exception:

        break

