
# 🧠 Python OOP Lab Project

This project is an object-oriented programming (OOP) simulation written in Python.  
It models a real-life scenario of employees, cars, and an office environment, and is based on lab requirements provided by ITI.

---

## 📘 Story

> "Samy is an employee. He works in ITI and owns a Fiat 128 car.  
> He goes every day (except weekends) to ITI Smart Village Office, which is 20km away."

The project simulates Samy's (and other employees') day-to-day life including sleeping, eating, working, driving, being late, and getting rewarded or punished.

---

## 📦 Features & Classes

### ✅ `Person`
- Attributes: `name`, `money`, `mood`, `healthRate`
- Methods: `sleep(hours)`, `eat(meals)`, `buy(items)`

### ✅ `Car`
- Attributes: `name`, `fuel_rate`, `velocity`
- Methods: `run(velocity, distance)`, `stop()`
- Velocity range: `0-200`, Fuel Rate range: `0-100`

### ✅ `Employee` (inherits from `Person`)
- Attributes: `id`, `car`, `email`, `salary`, `distanceToWork`
- Methods: `work(hours)`, `drive(distance, velocity)`, `refuel(gasAmount)`, `send_mail(...)`

### ✅ `Office`
- Attributes: `name`, `employees`
- Methods:  
  `hire()`, `fire()`, `deduct()`, `reward()`,  
  `get_all_employees()`, `get_employee(id)`,  
  `check_lateness(empId, moveHour)`,  
  `calculate_lateness(...)` *(static)*  
- Class Attributes: `employeesNum`, `change_emps_num(num)` *(classmethod)*

---

## 🧪 Testing

The `main.py` includes scenarios like:
- Hiring employees
- Driving cars to work
- Checking if employees are late
- Employee actions (sleep, eat, buy)
- Sending emails

You can run the test file using:
```bash
python main.py
```

---

## 📂 File Structure

```
OOP-Lab/
│
├── my_class.py
├── main.py         # test script
└── README.md
```

---


