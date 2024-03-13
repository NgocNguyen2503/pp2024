class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name