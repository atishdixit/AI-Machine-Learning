## Aproach Better even
class SingleTon:
    __instance = None

    def __init__(self):
        if SingleTon.__instance != None:
            raise Exception("Sigle to ")
        else:
            SingleTon.__instance = self

    @staticmethod
    def getInstance():
        if SingleTon.__instance == None:
            SingleTon()
        return SingleTon.__instance


s1 = SingleTon.getInstance()
s2 = SingleTon.getInstance()
print(s1)
print(s2)

class SingleTon1:
    __Instance = None

    def __new__(cls):
        if cls.__Instance is None:
            cls.__Instance = super(SingleTon1, cls).__new__(cls)
        return cls.__Instance


s11= SingleTon1()
s22 = SingleTon1()
print(s11)
print(s22)