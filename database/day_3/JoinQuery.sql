--1
select Dnum , Dname , SSN , Fname +' '+Lname as name 
from Departments
inner join Employee 
on Employee.SSN = Departments.MGRSSN


--2
select Dname, Pname
from Project 
inner join Departments 
on Departments.Dnum = Project.Dnum


--3
select d.*, Fname +' '+Lname as name 
from Dependent d
left outer join Employee 
on Employee.SSN = d.ESSN


--4
select Pnumber , Pname , Plocation 
from Project 
where city in ('Cairo','Alex')


--5
select * from Project 
where Pname like 'a%'


--6
select * from Employee 
where Dno=30 and Salary between 1000 and 2000


--7
select Fname +' '+Lname as name 
from Employee 
inner join Works_for 
on Employee.SSN = Works_for.ESSn and Hours >=10 
inner join Project 
on Project.Pnumber = Works_for.Pno and Project.Pname ='AL Rabwah'


--8
SELECT a.Fname +' '+a.Lname as name 
FROM Employee a , Employee b
where a.Superssn = b.SSN
AND b.Fname +' '+b.Lname ='Kamel Mohamed'


--9
select Fname +' '+Lname as name , Pname 
from Employee 
inner join Works_for 
on Employee.SSN = Works_for.ESSn 
inner join Project 
on Project.Pnumber = Works_for.Pno 
order by Pname


--10
select p.Pnumber, d.Dname , e.Lname, Address,Bdate 
from Project p
inner join Departments d
on p.Dnum = d.Dnum and city = 'Cairo' 
inner join Employee e
on e.SSN = d.MGRSSN


--11
SELECT DISTINCT a.*
FROM Employee a
JOIN Departments d ON a.Superssn = d.MGRSSN;


--12
select e.* ,d.* 
from Dependent d
right outer join Employee e
on e.SSN = d.ESSN


--13
insert into Employee  
([Fname],[Lname],[SSN],[Bdate],[Address],[Sex],[Salary],[Superssn],[Dno])
VALUES('Mostafa','Ismail',102672,'05-07-2001','EGY','M',3000,112233,30)


--14
insert into Employee  
([Fname],[Lname],[SSN],[Bdate],[Address],[Sex],[Dno])
VALUES('Aly','Ismail',102660,'12-17-1995','EGY','M',30)


--15
update Employee
set salary += Salary*.2
where SSN =102672