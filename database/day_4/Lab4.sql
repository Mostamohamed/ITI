--1
select d.Dependent_name , d.Sex 
from Dependent d
inner join Employee e
on e.SSN = d.ESSN and e.Sex='F' and d.Sex='F'
union all
select d.Dependent_name , d.Sex 
from Dependent d
inner join Employee e
on e.SSN = d.ESSN and e.Sex='M' and d.Sex='M'




--2
select p.Pname , sum(w.Hours) as HourPerWeek 
from project p
left join Works_for w
on p.Pnumber = w.Pno 
group by Pname




--3
select d.*  
from Employee e
inner join Departments d
on d.Dnum = e.Dno 
where e.SSN =(select min(SSN) from Employee )





--4
select d.Dname , min(e.Salary) as minSalary ,
max(e.Salary) as maxSalary,avg(e.Salary) as avgSalary 
from Departments d
left join Employee e
on d.Dnum = e.Dno
group by Dname





--5
select e.Fname +' '+e.Lname as name , e.SSN 
FROM Employee e 
inner join Departments d
on e.SSN = d.MGRSSN and not exists 
(select * from Dependent 
where d.MGRSSN = Dependent.ESSN)







--6.
select d.Dname,d.Dnum, count(e.SSN) ,avg(e.Salary) as avgSalary 
from Departments d
left join Employee e
on d.Dnum = e.Dno
group by Dname,Dnum
having avg(Salary) <(select avg(salary) from Employee)









--7
select Fname +' '+Lname as name , Pname , d.Dnum 
FROM Employee   e 
inner join Works_for  w 
on e.SSN = w.ESSn 
inner join Project  p 
on w.Pno = p.Pnumber 
inner join Departments  d 
on d.Dnum = p.Dnum
order by d.Dnum , Lname,Fname






--8
select top(2)salary as maxSalary 
from Employee 
where salary in (select max(salary) 
					from Employee 
					group by Dno )order by maxSalary desc 




--9
select distinct Fname +' '+Lname as Fullname , d.Dependent_name 
from Employee e 
inner join Dependent d 
on e.SSN = d.ESSN  
where d.Dependent_name like '%'+Fname +' '+Lname+'%'








--10
select Fname +' '+Lname as name , SSN 
FROM Employee e 
where  exists (select * 
from Dependent where e.SSN = Dependent.ESSN)





--11
insert into Departments values('DEPT IT',100,112233,'1-11-2006')




--12
update Departments
set MGRSSN = 968574
,[MGRStart Date]=GETDATE()
where Dnum =100

update Departments
set MGRSSN = 102672
,[MGRStart Date]=GETDATE()
where Dnum =20

update Employee
set Dno = 20
where SSN=102672

update Employee
set Superssn = 102672
where SSN=102660





--13
delete from Dependent where ESSN=223344
update Departments
set MGRSSN = 102672
where MGRSSN =223344

update Employee
set Superssn = 102672
where Superssn =223344

update Works_for
set ESSn = 102672
where ESSn =223344

delete from Employee where SSN=223344




--14
update Employee 
set Salary += Salary*.3
from Employee e 
inner join Works_for w 
on e.SSN= w.ESSn 
inner join Project p 
on p.Pnumber = w.Pno and p.Pname='Al Rabwah'