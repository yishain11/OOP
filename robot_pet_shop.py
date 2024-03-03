### where is the interactivity?
### where is the robot status change? why not in the class itself?

class robot:
    def __init__(self,name,id,battery_type,in_repair = False,
                 for_sale = True ,broken= False, 
                 prepared_to_be_shipped=False ,sold = False):
        pass
    def print(self):
        print(self.name,self.id,self.bettery_type)

    def print_robot_details(self):
        pass


class animal_robot(robot):
    def __init__(self, name, id, battery_type ,main_material,
                 price,cost_to_fix_per_day,animal_type):
        super().__init__(name, id, battery_type)
        self.main_material= main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.animal_type = animal_type
        

    def print_robot_details(self):
        print(self.name,self.id ,self.battery_type,
              self.main_material,
        self.price ,
        self.cost_to_fix_per_day,
        self.animal_type )


class employee_robot(robot):
    def __init__(self, name, id, battery_type, daily_salary):
        super().__init__(name, id, battery_type)
        self.daily_salary = daily_salary

    def print_robot_details(self):
        print(self.name,self.id ,self.battery_type,
               self.daily_salary)





class store:
    def __init__(self,balance,employees,pets) -> None:
        self.balance = balance
        self.employees = employees
        self.pets = pets


    def calculte_daily_employees_salary_cost(self):
        cost = 0
        for employee in self.employees:
            cost += employee.daily_salary
        return cost

    

    def go_to_repair(self, robot):
        for r in self.pets:
            ### is this the correct way to compare?
            if r==robot:
                balance -= r.cost_to_fix_per_day
                r.for_sale = False
                r.broken = True
                r.in_repair = True
         

    def end_of_day(self):
        ### is this the right way? what happens when you call function without ()?
        self.balance -= self.calculte_daily_employees_salary_cost

    def buy_a_robot(self, robot):
        for r in self.pets:
            if r == robot and robot.for_sale:
                r.for_sale = False
                r.sold = True
                self.balance += robot.price


    def print_store_balance(self):
        print(self.balance)

    def print_robot_details_by_id_or_name(self,idOrName):
        for r in self.pets:
            if r.id == idOrName or r.name == idOrName:
                r.print_robot_details()

    def print_all_employees_salary_cost(self):
        print(self.calculte_daily_employees_salary_cost)

 
    def print_for_sale_pets(self):
        for r in self.pets:
            if r.for_sale:
                r.print()
    
    def print_all_robots_in_repair(self):
        for r in self.pets:
            if r.in_repair:
                r.print()

        for r in self.employees:
            if r.in_repair:
                r.print()

    def print_for_sale_pets_in_range(self,min,max):
        for r in self.pets:
            if r.for_sale and r.price >=min and r.price <= max:
                r.print()


    
    
