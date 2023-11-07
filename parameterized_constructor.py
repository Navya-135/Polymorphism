class Employee:
    __fName:str=""
    __lName:str=""
    def __init__(self,fName,lName):
        self.__fName= fName
        self.__lName=lName
    def fullName(self):
        print(self.__fName+self.__lName)
emp=Employee("Navya","Kolakani")
emp.fullName()
