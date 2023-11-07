class Employee:
    __amt=40000
    def sal(self):
        return self.__amt*4
class ContractEmployee(Employee):
    __hrpay=1000
    __hrs=10
    def sal(self):
        return self.__hrpay*self.__hrs
emp=ContractEmployee()
print(emp.sal())

