SELECT * FROM Employee;

SELECT Fname , Lname , Salary , Dno FROM Employee;

SELECT Pname,Plocation ,Dnum FROM Project;

SELECT Fname +' '+ Lname AS full_name, Salary * 12 * 0.10 AS ANNUAL_COMM FROM Employee;

SELECT SSN ,Fname +' '+ Lname AS full_name  FROM Employee
WHERE Salary > 1000;

SELECT SSN ,Fname +' '+ Lname AS full_name  FROM Employee
WHERE Salary > 10000;

SELECT Fname +' '+ Lname AS full_name  FROM Employee
WHERE Sex = 'F';

SELECT Dnum , Dname FROM Departments
WHERE MGRSSN = '968574';

SELECT Pnumber,Pname,Plocation FROM Project
WHERE Dnum='10';
