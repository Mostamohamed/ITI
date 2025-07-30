class Person:
    def __init__(self, name, money, mood="neutral", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate
        
    def sleep(self,hours):
        if hours == 7:
            self.mood="happy"
        elif hours < 7:
            self.mood="tired"
        else:
            self.mood="lazy"
        
        print(f"{self.name} slept for {hours} hours and is now {self.mood}.")
        return self.mood
    
    def eat(self,meals):
        if meals == 3:
            self.healthRate=100
        elif meals == 2:
            self.healthRate=75
        elif meals == 1:
            self.healthRate=50
        else:
            self.healthRate =  max(0, self.healthRate - 10)
         
        print(f"{self.name} ate {meals} meals. Health rate is now {self.healthRate}%.")    
        return self.healthRate
    
    def buy(self,items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} bought {items} item(s) and has {self.money} L.E left.")
            return "Done"
        else:
            print(f"{self.name} can't afford {items} item(s). Needs {cost} L.E but has {self.money}.")
            return "Not enough money"













class Car():
    def __init__(self, name,fuel_rate=100 , velocity=0):
        self.name=name
        self._fuel_rate = fuel_rate
        self._velocity = velocity
        self.remaining_distance = 0
        
    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        self._fuel_rate = min(max(0, value), 100)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = min(max(0, value), 200)    
    
    
    def run(self,velocity,distance):
        self.velocity=velocity
        max_distance=self.fuel_rate
        if distance <= max_distance:
            self.fuel_rate-=distance
            self.remaining_distance=0
            print(f"Driving {max_distance} at velocity {velocity}")
        else:
            self.remaining_distance=distance-max_distance
            self.fuel_rate=0
            print(f"Driving {max_distance} at velocity {velocity}")
    
        self.stop()
        
    def stop(self):
        self.velocity=0
        if self.remaining_distance == 0:
            print("You have arrived at your destination!")
        else:
            print(f"You have stopped with {self.remaining_distance}Km remaining to your destination.")













class Employee(Person):
    def __init__(self, name, money, mood, healthRate,id , car,email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)   
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    
    def has_car(self):
        return self.car is not None
    
    def work(self,hours):
        if hours == 8:
            self.mood="happy"
        elif hours < 8:
            self.mood="lazy"
        else:
            self.mood="tired"
            
        print(f"{self.name} worked {hours} hours and now feels {self.mood}.")
        return self.mood
    
    def drive(self, distance, velocity):
        if self.has_car():
            self.car.run(distance, velocity)
        else:
            print(f"{self.name} doesn't have a car.")
        
    def refuel(self,gasAmount=100):
        if self.has_car():
            if gasAmount < 0:
                print("Invalid gas amount.")
                return
            self.car.fuel_rate += gasAmount
            print(f"New fuel rate: {self.car.fuel_rate}")
        else:
            print(f"{self.name} can't refuel — no car assigned.")
        
    def send_mail(self,to,subject,body):
        print(f"Email sent from {self.email} to {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")













class Office():
    employeesNum = 0
    
    def __init__(self, name):
        self.name=name
        self.employees=[]
    
    @classmethod
    def get_emps_num(cls):
        return cls.employeesNum
        
    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num   
    
    def get_all_employees(self):
        return self.employees
        
    def get_employee(self,empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None 
        
    def hire(self,employee):
        self.employees.append(employee)
        Office.employeesNum+=1
        print(f"{employee.name} has been hired to {self.name}.")
        
        
    def fire(self,empId):
        for emp in self.employees:
            if emp.id == empId:
                self.employees.remove(emp)
                Office.employeesNum-=1
                print(f"{emp.name} (ID: {empId}) has been fired.")
                return
            
        print(f"(ID: {empId}) Not Found.")
                
        
    def deduct(self,empId,deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"{deduction} L.E has been deducted from {emp.name}'s salary.")
        else:
            print(f"Employee with ID {empId} not found.")
        
    def reward(self,empId,reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"{reward} L.E has been added to {emp.name}'s salary.")
        else:
            print(f"Employee with ID {empId} not found.")   
        
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        time = distance / velocity
        moveHour+= time
        if targetHour > moveHour:
            return False  # مش متاخر
        else :
            return True   # متاخر
        
    def check_lateness(self,empId, moveHour):
        emp=self.get_employee(empId)
        targetHour = 9
        money = 10 
        if emp:
            velocity = emp.car.velocity if emp.has_car() else 60
            is_late=Office.calculate_lateness(targetHour,moveHour,emp.distanceToWork,velocity)
            
            if is_late:
                self.deduct(empId,money)
                print(f"{emp.name} is late. Deducted {money}  from salary.")
            else:
                self.reward(empId,money)
                print(f"{emp.name} is on time. Rewarded  {money}  to salary.")

        else:
            print(f"Employee with ID {empId} not found.")
            
           
            
    
        