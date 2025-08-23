USE ITI

--1
select count(St_Id) as StudentCount
from Student 
where St_Age is not null

--2
select distinct Ins_Name as Instructor_Name
from Instructor

--3
select St_Id 'student id', isnull(St_Fname+' '+St_Lname,'Student Full name') 'Student Full Name',d.Dept_Name 'Department name'
from Student e
inner join Department d
on d.Dept_Id=e.Dept_Id

--4 
select Ins_Name Instructor_name, d.Dept_Name department_name
from Instructor i
left join Department d
on d.Dept_Id=i.Dept_Id

--5
select St_Fname+' '+St_Lname as 'Student Full Name' , Crs_Name as 'Course Name' 
from Student 
inner join Stud_Course 
on Student.St_Id =Stud_Course.St_Id
inner join Course
on Course.Crs_Id=Stud_Course.Crs_Id and Grade is not null


--6
select count(Crs_Id) 'Number of Courses',Top_Name  
from Course 
inner join Topic 
on Course.Top_Id = Topic.Top_Id 
group by Top_Name

--7
select min(salary) as 'Min Salary',max(salary) as 'Max Salary'	
from Instructor

--8

select *  
from Instructor 
where Salary < (select avg(Salary) from Instructor)

--9

select Dept_Name as'Department name' 
from Department 
inner join Instructor 
on Department.Dept_Id = Instructor.Dept_Id and Salary =(select min(Salary) from Instructor)

--10

select top(2) salary 
from Instructor 
order by Salary desc

--11

select Ins_Name as InstuctorName, coalesce(convert(nvarchar(20),salary),'instructor bonus') as Salary 
from Instructor 

--12

select avg(salary) as AvgSalary 
from Instructor

--13

select s.St_Fname as StudentFirstName , super.*  
from student as s 
inner join student super
on s.St_super = super.St_Id

--14.

select * 
from (select salary,Dept_Id, ROW_NUMBER() over (partition by Dept_Id order by salary) as rk 
from instructor where salary is not null)
as newtable where rk <=2

--15.

select * 
from (select *, rank() over (partition by Dept_Id order by newid()) as rk from Student)
as newtable where rk <2
