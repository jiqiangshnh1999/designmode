#
# author jiqiang
# 观察者模式
#


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

    def notify(self, observer):
        for o in observer:
            o.notify(self.__temperature)


class Observer:

    def __init__(self):
        pass


class WaterMood(Observer):

    def notify(self, temperature):
        if temperature >= 100:
            print("可以喝水了！")


class ShowerMood(Observer):

    def notify(self, temperature):
        if temperature > 70:
            print('可以洗澡了！')


class TestClass:

    def __init__(self):
        thing = HeatWater()
        water = WaterMood()
        shower = ShowerMood()

        thing.addObserver(water)
        thing.addObserver(shower)

        obv = thing.getObserver()

        thing.setTemperature(100)

        thing.notify(obv)


TestClass()

