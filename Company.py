from Employee import Employee


class Company():
    name=""
    employees=[]
    
    def set_name(self,name: str):
        self.name=name

    def get_name(self):
        a=[
            ["asdasdasd",4,5],
            [1,2,3.254]
        ]
        return a
        a=1+2
        b=a+2
        return b
    
    def add_employee(self,em:Employee):
        self.employees.append(em)        
    def show_employees(self):
        print(self.employees)
    def remove_employee(self,em:str):
        for value in self.employees:
            if value.name==em:
                self.employees.remove(value)
                break
            