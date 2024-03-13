import numpy as np


class Student:
    def __init__(self,id,name,dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.mark = {}

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob
    
    def gpa_cal(self):
        mark_arr = np.array(list(self.mark.values()))
        incomplete = False
        for i in mark_arr:
            if i == None:
                incomplete = True
                break
        if incomplete == True:
            print("Missing some courses")
        else:
            gpa = np.sum(mark_arr)/len(mark_arr)
            return gpa

    def course_joining(self):
        course_arr = np.array(list(self.mark.keys()))
        return course_arr
 