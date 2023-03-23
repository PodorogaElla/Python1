'''
2.реализовать метакласс, позволяющий создавать всегда один и тот же объект класса (см. урок)
'''

class DocMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = []        

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        
class MyClass (metaclass=DocMeta):
	pass
obj_1 = MyClass()
obj_2 = MyClass()
print (obj_1 is obj_2)

