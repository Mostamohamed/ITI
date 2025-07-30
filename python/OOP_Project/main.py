from my_class import *

print("test with information in document")

car1 = Car("Fiat 128", fuel_rate=100, velocity=0)
samy = Employee(name="Samy", money=1000, mood="neutral", healthRate=100,
                id=1, car=car1, email="samy@example.com", salary=5000, distanceToWork=20)


iti = Office("ITI Smart Village")


iti.hire(samy)


samy.drive(distance=20, velocity=40)


iti.check_lateness(empId=1, moveHour=8)



print("End test with information in document")

#####################################################

# create car
car1 = Car(name="Toyota", fuel_rate=50, velocity=60)

# employee with car
emp1 = Employee(
    name="Ahmed", money=1000, mood="neutral", healthRate=90,
    id=1, car=car1, email="ahmed@example.com", salary=5000, distanceToWork=30
)

#  employee without car
emp2 = Employee(
    name="Sara", money=800, mood="neutral", healthRate=85,
    id=2, car=None, email="sara@example.com", salary=4800, distanceToWork=25
)

#  office and hire
office = Office("ITI Office")
office.hire(emp1)
office.hire(emp2)

#  list all employee
print("\nAll Employees:")
for emp in office.get_all_employees():
    print(f"{emp.name} - ID: {emp.id}")

# check for lateness
print("\nChecking Lateness:")
office.check_lateness(empId=1, moveHour=7.5)  # Ahmed
office.check_lateness(empId=2, moveHour=8.2)  # Sara

# Testing Employee Methods
print("\nTesting Employee Methods:")
emp1.sleep(7)
emp1.eat(3)
emp1.buy(2)
emp1.drive(30, 60)
emp1.refuel(20)
emp1.send_mail("boss@iti.org", "Late Report", "I was on time today.")

emp2.sleep(6)
emp2.eat(2)
emp2.buy(1)
emp2.drive(25, 50)  # ماعندهاش عربية
emp2.refuel()       # ماعندهاش عربية
emp2.send_mail("hr@iti.org", "Leave Request", "I need a day off.")
